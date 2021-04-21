import jwt
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import json
from datetime import datetime, timedelta
import grpc
import trillian_admin_api_pb2_grpc
import trillian_admin_api_pb2
import crypto.keyspb.keyspb_pb2
from google.protobuf import duration_pb2
import trillian_log_api_pb2_grpc
import trillian_log_api_pb2



class AuthorizationServer:

    
    def __init__(self, key_pair, issuer_uri):
        '''Initialize the authorization server with its key pair and the token count'''
        self.sk = key_pair[0].private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.PKCS8,
                                            encryption_algorithm=serialization.
                                            BestAvailableEncryption(password=b'password'))

        self.pk = key_pair[1].public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo)
        self.issuer_uri = issuer_uri
        self.id = 0


    @classmethod
    def generate_key(cls):
        sk = ec.generate_private_key(curve = ec.SECP256R1())
        pk = sk.public_key()
        return sk,pk


    def generate_jwt(self, client='C', server='R', key_algorithm='ES256'):
        loaded_sk = serialization.load_pem_private_key(self.sk, password=b'password')
        token = jwt.encode(payload={'id':self.id, 'client':client, 'server':server,
                                    'iss':self.issuer_uri,
                                    'exp':datetime.utcnow()+timedelta(days=30),
                                    'nbf':datetime.utcnow()},
                           key=loaded_sk, algorithm=key_algorithm)
        self.id+=1
        return token



class Trillian:
    def __init__(self, key_pair, key_algorithm=['ES256','RS256'], allowed_servers=[]):
        '''Initialize the trillian personality with its key pair,
        the allowed algorithms and the dictionaries of the resource
        servers and clients that are added to the Merkle Tree. Start
        also the services to communicate with the Trillian server'''
        self.sk = key_pair[0].private_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PrivateFormat.PKCS8,
                                            encryption_algorithm=serialization.
                                            BestAvailableEncryption(password=b'password2'))

        self.pk = key_pair[1].public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo)
        self.allowed_algorithms = key_algorithm
        self.allowed_servers = allowed_servers
        self.server = {}
        self.clients = {}
        #Open the connection with the Trillian server and the service to use the API
        channel = grpc.insecure_channel('localhost:8090')
        self.stub = trillian_admin_api_pb2_grpc.TrillianAdminStub(channel)
        self.stub2 = trillian_log_api_pb2_grpc.TrillianLogStub(channel)
        #Create the three and initialize it
        self.tree_id = self.create_tree()
        self.init_log(self.tree_id)


    @classmethod
    def generate_key(cls):
        sk = ec.generate_private_key(curve = ec.SECP256R1())
        pk = sk.public_key()
        return sk,pk


    def create_tree(self):
        '''Create the tree'''
        time = duration_pb2.Duration(seconds=3600)
        response = self.stub.CreateTree(trillian_admin_api_pb2. \
        CreateTreeRequest(tree={"tree_state":'ACTIVE',"tree_type":'LOG', \
        "hash_strategy":'RFC6962_SHA256', "hash_algorithm":'SHA256', \
        "signature_algorithm":'ECDSA', "display_name":'', \
        "description":'',"max_root_duration":time}, \
        key_spec=crypto.keyspb.keyspb_pb2.Specification \
        (ecdsa_params={"curve":'P256'})))
        return response.tree_id


    def init_log(self,tree_id):
        '''Log to initialize the tree'''
        response = self.stub2.InitLog(trillian_log_api_pb2. \
        InitLogRequest(log_id=tree_id, \
        charge_to=trillian_log_api_pb2.ChargeTo(user='test')))
        return response


    def queue_leaf(self,tree_id,leaf_value,extra_data=''):
        '''Insert a leaf in the tree'''
        response = self.stub2.QueueLeaf(trillian_log_api_pb2. \
        QueueLeafRequest(log_id=tree_id, \
        leaf={'leaf_value':f'{leaf_value}'.encode(),'extra_data':f'{extra_data}'.encode()}))
        return response


    def inclusion_proof(self,tree_id,leaf_id):
        '''Return the inclusion proof for a leaf, indicated with his id,
        for a specific size of the tree'''
        response = self.stub2.GetInclusionProof(trillian_log_api_pb2. \
        GetInclusionProofRequest(log_id=tree_id, \
        leaf_index=leaf_id, tree_size=(leaf_id+1)))
        return response


    def update_info(self,data):
        '''Update the dictionary of clients and servers that are added
        to the log'''
        if data["server"] in self.server.keys():
            self.server[data["server"]].append([data["client"], data["id"],
                                                data["nbf"], data["exp"]])
        else:
            self.server[data["server"]] = [[data["client"], data["id"],
                                            data["nbf"], data["exp"]]]
        if data["client"] in self.clients.keys():
            self.clients[data["client"]].append([data["server"], data["id"],
                                                 data["nbf"], data["exp"]])
        else:
            self.clients[data["client"]] = [[data["server"], data["id"],
                                             data["nbf"], data["exp"]]]


    def decode_jwt(self, token, authorization_server_pk):
        '''Decode a JWT'''
        try:
            data = jwt.decode(jwt=token, key=authorization_server_pk, issuer=self.allowed_servers,
                              algorithms=self.allowed_algorithms, options={"verify_iss":True,
                                                                           "require_exp":True,
                                                                           "verify_exp":True,
                                                                           "require_nbf":True})
            return data
        except jwt.exceptions.InvalidIssuerError:
            print("Invalid issuer")
            return
        except jwt.exceptions.ExpiredSignatureError:
            print("The token has expired")
            return
        except jwt.exceptions.ImmatureSignatureError:
            print("The validity of the token has not started")
        except jwt.exceptions.InvalidTokenError:
            print("Invalid token")
            return


    def insert_jwt(self, token, authorization_server):
        data = self.decode_jwt(token, authorization_server.pk)
        print(data)
        if data != None:
            #leaf_value = {'client':data["client"], 'server':data["server"]}
            #leaf_value_serialize = list(sorted(leaf_value.items()))
            leaf_value = json.dumps({'client':data["client"], 'server':data["server"]},
                                    sort_keys=True)
            leaf_id = data["id"]
            print(f'Leaf value: {leaf_value}')
            leaf_added = self.queue_leaf(self.tree_id, leaf_value)
            print(f'Leaf added:\n{leaf_added}')
            if leaf_added.queued_leaf.leaf.leaf_index != -1:
                self.update_info(data)
            else:
                print("Leaf already present in the log")
                authorization_server.id-=1
            inclusion_proof = self.inclusion_proof(self.tree_id,leaf_id)
            print(f'Inclusion Proof:\n{inclusion_proof}')


    def check_server(self, server):
        '''Check if a server is in the log and, if it is, print clients
        that are allowed to access it'''
        try:
            return self.server[f"{server}"]
        except KeyError:
            print("The server is not present in the log")


    def check_client(self, client):
        '''Check if a client is in the log and, if it is, print servers
        that he has permission to access'''
        try:
            return self.clients[f"{client}"]
        except:
            print("The client is not present in the log")
