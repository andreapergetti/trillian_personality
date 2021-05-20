# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import trillian_log_api_pb2 as trillian__log__api__pb2


class TrillianLogStub(object):
    """The TrillianLog service provides access to an append-only Log data structure
    as described in the [Verifiable Data
    Structures](docs/papers/VerifiableDataStructures.pdf) paper.

    The API supports adding new entries to the Merkle tree for a specific Log
    instance (identified by its log_id) in two modes:
    - For a normal log, new leaf entries are queued up for subsequent
    inclusion in the log, and the leaves are assigned consecutive leaf_index
    values as part of that integration process.
    - For a 'pre-ordered log', new entries have an already-defined leaf
    ordering, and leaves are only integrated into the Merkle tree when a
    contiguous range of leaves is available.

    The API also supports read operations to retrieve leaf contents, and to
    provide cryptographic proofs of leaf inclusion and of the append-only nature
    of the Log.

    Each API request also includes a charge_to field, which allows API users
    to provide quota identifiers that should be "charged" for each API request
    (and potentially rejected with codes.ResourceExhausted).

    Various operations on the API also allows for 'server skew', which can occur
    when different API requests happen to be handled by different server instances
    that may not all be up to date.  An API request that is relative to a specific
    tree size may reach a server instance that is not yet aware of this tree size;
    in this case the server will typically return an OK response that contains:
    - a signed log root that indicates the tree size that it is aware of
    - an empty response otherwise.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueueLeaf = channel.unary_unary(
                '/trillian.TrillianLog/QueueLeaf',
                request_serializer=trillian__log__api__pb2.QueueLeafRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.QueueLeafResponse.FromString,
                )
        self.AddSequencedLeaf = channel.unary_unary(
                '/trillian.TrillianLog/AddSequencedLeaf',
                request_serializer=trillian__log__api__pb2.AddSequencedLeafRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.AddSequencedLeafResponse.FromString,
                )
        self.GetInclusionProof = channel.unary_unary(
                '/trillian.TrillianLog/GetInclusionProof',
                request_serializer=trillian__log__api__pb2.GetInclusionProofRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetInclusionProofResponse.FromString,
                )
        self.GetInclusionProofByHash = channel.unary_unary(
                '/trillian.TrillianLog/GetInclusionProofByHash',
                request_serializer=trillian__log__api__pb2.GetInclusionProofByHashRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetInclusionProofByHashResponse.FromString,
                )
        self.GetConsistencyProof = channel.unary_unary(
                '/trillian.TrillianLog/GetConsistencyProof',
                request_serializer=trillian__log__api__pb2.GetConsistencyProofRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetConsistencyProofResponse.FromString,
                )
        self.GetLatestSignedLogRoot = channel.unary_unary(
                '/trillian.TrillianLog/GetLatestSignedLogRoot',
                request_serializer=trillian__log__api__pb2.GetLatestSignedLogRootRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetLatestSignedLogRootResponse.FromString,
                )
        self.GetSequencedLeafCount = channel.unary_unary(
                '/trillian.TrillianLog/GetSequencedLeafCount',
                request_serializer=trillian__log__api__pb2.GetSequencedLeafCountRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetSequencedLeafCountResponse.FromString,
                )
        self.GetEntryAndProof = channel.unary_unary(
                '/trillian.TrillianLog/GetEntryAndProof',
                request_serializer=trillian__log__api__pb2.GetEntryAndProofRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetEntryAndProofResponse.FromString,
                )
        self.InitLog = channel.unary_unary(
                '/trillian.TrillianLog/InitLog',
                request_serializer=trillian__log__api__pb2.InitLogRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.InitLogResponse.FromString,
                )
        self.QueueLeaves = channel.unary_unary(
                '/trillian.TrillianLog/QueueLeaves',
                request_serializer=trillian__log__api__pb2.QueueLeavesRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.QueueLeavesResponse.FromString,
                )
        self.AddSequencedLeaves = channel.unary_unary(
                '/trillian.TrillianLog/AddSequencedLeaves',
                request_serializer=trillian__log__api__pb2.AddSequencedLeavesRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.AddSequencedLeavesResponse.FromString,
                )
        self.GetLeavesByIndex = channel.unary_unary(
                '/trillian.TrillianLog/GetLeavesByIndex',
                request_serializer=trillian__log__api__pb2.GetLeavesByIndexRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetLeavesByIndexResponse.FromString,
                )
        self.GetLeavesByRange = channel.unary_unary(
                '/trillian.TrillianLog/GetLeavesByRange',
                request_serializer=trillian__log__api__pb2.GetLeavesByRangeRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetLeavesByRangeResponse.FromString,
                )
        self.GetLeavesByHash = channel.unary_unary(
                '/trillian.TrillianLog/GetLeavesByHash',
                request_serializer=trillian__log__api__pb2.GetLeavesByHashRequest.SerializeToString,
                response_deserializer=trillian__log__api__pb2.GetLeavesByHashResponse.FromString,
                )


class TrillianLogServicer(object):
    """The TrillianLog service provides access to an append-only Log data structure
    as described in the [Verifiable Data
    Structures](docs/papers/VerifiableDataStructures.pdf) paper.

    The API supports adding new entries to the Merkle tree for a specific Log
    instance (identified by its log_id) in two modes:
    - For a normal log, new leaf entries are queued up for subsequent
    inclusion in the log, and the leaves are assigned consecutive leaf_index
    values as part of that integration process.
    - For a 'pre-ordered log', new entries have an already-defined leaf
    ordering, and leaves are only integrated into the Merkle tree when a
    contiguous range of leaves is available.

    The API also supports read operations to retrieve leaf contents, and to
    provide cryptographic proofs of leaf inclusion and of the append-only nature
    of the Log.

    Each API request also includes a charge_to field, which allows API users
    to provide quota identifiers that should be "charged" for each API request
    (and potentially rejected with codes.ResourceExhausted).

    Various operations on the API also allows for 'server skew', which can occur
    when different API requests happen to be handled by different server instances
    that may not all be up to date.  An API request that is relative to a specific
    tree size may reach a server instance that is not yet aware of this tree size;
    in this case the server will typically return an OK response that contains:
    - a signed log root that indicates the tree size that it is aware of
    - an empty response otherwise.
    """

    def QueueLeaf(self, request, context):
        """QueueLeaf adds a single leaf to the queue of pending leaves for a normal
        log.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSequencedLeaf(self, request, context):
        """AddSequencedLeaf adds a single leaf with an assigned sequence number to a
        pre-ordered log.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInclusionProof(self, request, context):
        """GetInclusionProof returns an inclusion proof for a leaf with a given index
        in a particular tree.

        If the requested tree_size is larger than the server is aware of, the
        response will include the latest known log root and an empty proof.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInclusionProofByHash(self, request, context):
        """GetInclusionProofByHash returns an inclusion proof for any leaves that have
        the given Merkle hash in a particular tree.

        If any of the leaves that match the given Merkle has have a leaf index that
        is beyond the requested tree size, the corresponding proof entry will be empty.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConsistencyProof(self, request, context):
        """GetConsistencyProof returns a consistency proof between different sizes of
        a particular tree.

        If the requested tree size is larger than the server is aware of,
        the response will include the latest known log root and an empty proof.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestSignedLogRoot(self, request, context):
        """GetLatestSignedLogRoot returns the latest signed log root for a given tree,
        and optionally also includes a consistency proof from an earlier tree size
        to the new size of the tree.

        If the earlier tree size is larger than the server is aware of,
        an InvalidArgument error is returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSequencedLeafCount(self, request, context):
        """GetSequencedLeafCount returns the total number of leaves that have been
        integrated into the given tree.

        DO NOT USE - FOR DEBUGGING/TEST ONLY

        (Use GetLatestSignedLogRoot then de-serialize the Log Root and use
        use the tree size field within.)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntryAndProof(self, request, context):
        """GetEntryAndProof returns a log leaf and the corresponding inclusion proof
        to a specified tree size, for a given leaf index in a particular tree.

        If the requested tree size is unavailable but the leaf is
        in scope for the current tree, the returned proof will be for the
        current tree size rather than the requested tree size.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitLog(self, request, context):
        """InitLog initializes a particular tree, creating the initial signed log
        root (which will be of size 0).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueueLeaves(self, request, context):
        """QueueLeaf adds a batch of leaves to the queue of pending leaves for a
        normal log.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSequencedLeaves(self, request, context):
        """AddSequencedLeaves adds a batch of leaves with assigned sequence numbers
        to a pre-ordered log.  The indices of the provided leaves must be contiguous.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeavesByIndex(self, request, context):
        """GetLeavesByIndex returns a batch of leaves whose leaf indices are provided
        in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeavesByRange(self, request, context):
        """GetLeavesByRange returns a batch of leaves whose leaf indices are in a
        sequential range.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLeavesByHash(self, request, context):
        """GetLeavesByHash returns a batch of leaves which are identified by their
        Merkle leaf hash values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrillianLogServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'QueueLeaf': grpc.unary_unary_rpc_method_handler(
                    servicer.QueueLeaf,
                    request_deserializer=trillian__log__api__pb2.QueueLeafRequest.FromString,
                    response_serializer=trillian__log__api__pb2.QueueLeafResponse.SerializeToString,
            ),
            'AddSequencedLeaf': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSequencedLeaf,
                    request_deserializer=trillian__log__api__pb2.AddSequencedLeafRequest.FromString,
                    response_serializer=trillian__log__api__pb2.AddSequencedLeafResponse.SerializeToString,
            ),
            'GetInclusionProof': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInclusionProof,
                    request_deserializer=trillian__log__api__pb2.GetInclusionProofRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetInclusionProofResponse.SerializeToString,
            ),
            'GetInclusionProofByHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInclusionProofByHash,
                    request_deserializer=trillian__log__api__pb2.GetInclusionProofByHashRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetInclusionProofByHashResponse.SerializeToString,
            ),
            'GetConsistencyProof': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConsistencyProof,
                    request_deserializer=trillian__log__api__pb2.GetConsistencyProofRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetConsistencyProofResponse.SerializeToString,
            ),
            'GetLatestSignedLogRoot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestSignedLogRoot,
                    request_deserializer=trillian__log__api__pb2.GetLatestSignedLogRootRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetLatestSignedLogRootResponse.SerializeToString,
            ),
            'GetSequencedLeafCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSequencedLeafCount,
                    request_deserializer=trillian__log__api__pb2.GetSequencedLeafCountRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetSequencedLeafCountResponse.SerializeToString,
            ),
            'GetEntryAndProof': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntryAndProof,
                    request_deserializer=trillian__log__api__pb2.GetEntryAndProofRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetEntryAndProofResponse.SerializeToString,
            ),
            'InitLog': grpc.unary_unary_rpc_method_handler(
                    servicer.InitLog,
                    request_deserializer=trillian__log__api__pb2.InitLogRequest.FromString,
                    response_serializer=trillian__log__api__pb2.InitLogResponse.SerializeToString,
            ),
            'QueueLeaves': grpc.unary_unary_rpc_method_handler(
                    servicer.QueueLeaves,
                    request_deserializer=trillian__log__api__pb2.QueueLeavesRequest.FromString,
                    response_serializer=trillian__log__api__pb2.QueueLeavesResponse.SerializeToString,
            ),
            'AddSequencedLeaves': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSequencedLeaves,
                    request_deserializer=trillian__log__api__pb2.AddSequencedLeavesRequest.FromString,
                    response_serializer=trillian__log__api__pb2.AddSequencedLeavesResponse.SerializeToString,
            ),
            'GetLeavesByIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeavesByIndex,
                    request_deserializer=trillian__log__api__pb2.GetLeavesByIndexRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetLeavesByIndexResponse.SerializeToString,
            ),
            'GetLeavesByRange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeavesByRange,
                    request_deserializer=trillian__log__api__pb2.GetLeavesByRangeRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetLeavesByRangeResponse.SerializeToString,
            ),
            'GetLeavesByHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLeavesByHash,
                    request_deserializer=trillian__log__api__pb2.GetLeavesByHashRequest.FromString,
                    response_serializer=trillian__log__api__pb2.GetLeavesByHashResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trillian.TrillianLog', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrillianLog(object):
    """The TrillianLog service provides access to an append-only Log data structure
    as described in the [Verifiable Data
    Structures](docs/papers/VerifiableDataStructures.pdf) paper.

    The API supports adding new entries to the Merkle tree for a specific Log
    instance (identified by its log_id) in two modes:
    - For a normal log, new leaf entries are queued up for subsequent
    inclusion in the log, and the leaves are assigned consecutive leaf_index
    values as part of that integration process.
    - For a 'pre-ordered log', new entries have an already-defined leaf
    ordering, and leaves are only integrated into the Merkle tree when a
    contiguous range of leaves is available.

    The API also supports read operations to retrieve leaf contents, and to
    provide cryptographic proofs of leaf inclusion and of the append-only nature
    of the Log.

    Each API request also includes a charge_to field, which allows API users
    to provide quota identifiers that should be "charged" for each API request
    (and potentially rejected with codes.ResourceExhausted).

    Various operations on the API also allows for 'server skew', which can occur
    when different API requests happen to be handled by different server instances
    that may not all be up to date.  An API request that is relative to a specific
    tree size may reach a server instance that is not yet aware of this tree size;
    in this case the server will typically return an OK response that contains:
    - a signed log root that indicates the tree size that it is aware of
    - an empty response otherwise.
    """

    @staticmethod
    def QueueLeaf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/QueueLeaf',
            trillian__log__api__pb2.QueueLeafRequest.SerializeToString,
            trillian__log__api__pb2.QueueLeafResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSequencedLeaf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/AddSequencedLeaf',
            trillian__log__api__pb2.AddSequencedLeafRequest.SerializeToString,
            trillian__log__api__pb2.AddSequencedLeafResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInclusionProof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetInclusionProof',
            trillian__log__api__pb2.GetInclusionProofRequest.SerializeToString,
            trillian__log__api__pb2.GetInclusionProofResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInclusionProofByHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetInclusionProofByHash',
            trillian__log__api__pb2.GetInclusionProofByHashRequest.SerializeToString,
            trillian__log__api__pb2.GetInclusionProofByHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConsistencyProof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetConsistencyProof',
            trillian__log__api__pb2.GetConsistencyProofRequest.SerializeToString,
            trillian__log__api__pb2.GetConsistencyProofResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLatestSignedLogRoot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetLatestSignedLogRoot',
            trillian__log__api__pb2.GetLatestSignedLogRootRequest.SerializeToString,
            trillian__log__api__pb2.GetLatestSignedLogRootResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSequencedLeafCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetSequencedLeafCount',
            trillian__log__api__pb2.GetSequencedLeafCountRequest.SerializeToString,
            trillian__log__api__pb2.GetSequencedLeafCountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEntryAndProof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetEntryAndProof',
            trillian__log__api__pb2.GetEntryAndProofRequest.SerializeToString,
            trillian__log__api__pb2.GetEntryAndProofResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/InitLog',
            trillian__log__api__pb2.InitLogRequest.SerializeToString,
            trillian__log__api__pb2.InitLogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueueLeaves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/QueueLeaves',
            trillian__log__api__pb2.QueueLeavesRequest.SerializeToString,
            trillian__log__api__pb2.QueueLeavesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSequencedLeaves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/AddSequencedLeaves',
            trillian__log__api__pb2.AddSequencedLeavesRequest.SerializeToString,
            trillian__log__api__pb2.AddSequencedLeavesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLeavesByIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetLeavesByIndex',
            trillian__log__api__pb2.GetLeavesByIndexRequest.SerializeToString,
            trillian__log__api__pb2.GetLeavesByIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLeavesByRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetLeavesByRange',
            trillian__log__api__pb2.GetLeavesByRangeRequest.SerializeToString,
            trillian__log__api__pb2.GetLeavesByRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLeavesByHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trillian.TrillianLog/GetLeavesByHash',
            trillian__log__api__pb2.GetLeavesByHashRequest.SerializeToString,
            trillian__log__api__pb2.GetLeavesByHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
