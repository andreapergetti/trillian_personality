# trillian
To build and test Trillian you need:
- Go 1.14 or later
- MySQL or MariaDB to provide the data storage layer

To fetch the code, dependencies, and build Trillian, run the following:
```
export GO111MODULE=auto
git clone https://github.com/google/trillian.git --branch v1.3.13
cd trillian
go build ./...
```

For simple deployments, running in a container is an easy way to get up and running with a local database. To use Docker to run and interact with Trillian, use:
```
docker-compose -f examples/deployment/docker-compose.yml up
```

## Uso delle API
Install dependencies written in the Pipfile.lock file using pipenv:
```
pipenv install --ignore-pipfile
```
Installare le definizioni per il protocol buffer per le API di google:
```
git clone ssh://git@github.com/googleapis/googleapis.git \
$HOME/go/src/github.com/googleapis/googleapis
```
Copiare nella directory corrente:
```
cp -r $HOME/go/src/github.com/googleapis/googleapis/google .
```
Use protocol buffer compiler to produce Python output from the definitions of the protocol(file .proto). For every *namefile*.proto file in input, it generates *namefile*_pb2.py which contains our generated request and response classes and *namefile*_pb2_grpc.py which contains our generated client and server classes.
```
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. \
trillian_admin_api.proto \
trillian_log_api.proto	trillian.proto 

cd crypto/keyspb
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. keyspb.proto

cd crypto/sigpb
python3.8 -m grpc_tools.protoc \
--proto_path=. --python_out=. \
--grpc_python_out=. sigpb.proto
```
Afterwards, you can download the jupyter-notebook file in this repository, to see examples of use of the API.
