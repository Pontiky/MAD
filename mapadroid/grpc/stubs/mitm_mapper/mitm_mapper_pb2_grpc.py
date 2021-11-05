# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from mapadroid.grpc.compiled.mitm_mapper import mitm_mapper_pb2 as mitm__mapper_dot_mitm__mapper__pb2
from mapadroid.grpc.compiled.shared import Ack_pb2 as shared_dot_Ack__pb2
from mapadroid.grpc.compiled.shared import Worker_pb2 as shared_dot_Worker__pb2


class MitmMapperStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLastPossiblyMoved = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/GetLastPossiblyMoved',
                request_serializer=shared_dot_Worker__pb2.Worker.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LastMoved.FromString,
                )
        self.UpdateLatest = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/UpdateLatest',
                request_serializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryUpdateRequest.SerializeToString,
                response_deserializer=shared_dot_Ack__pb2.Ack.FromString,
                )
        self.RequestLatest = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/RequestLatest',
                request_serializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryRequest.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryResponse.FromString,
                )
        self.SetLevel = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/SetLevel',
                request_serializer=mitm__mapper_dot_mitm__mapper__pb2.SetLevelRequest.SerializeToString,
                response_deserializer=shared_dot_Ack__pb2.Ack.FromString,
                )
        self.SetPokestopVisits = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/SetPokestopVisits',
                request_serializer=mitm__mapper_dot_mitm__mapper__pb2.SetPokestopVisitsRequest.SerializeToString,
                response_deserializer=shared_dot_Ack__pb2.Ack.FromString,
                )
        self.GetPokestopVisits = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/GetPokestopVisits',
                request_serializer=shared_dot_Worker__pb2.Worker.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.PokestopVisitsResponse.FromString,
                )
        self.GetLevel = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/GetLevel',
                request_serializer=shared_dot_Worker__pb2.Worker.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LevelResponse.FromString,
                )
        self.GetInjectionStatus = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/GetInjectionStatus',
                request_serializer=shared_dot_Worker__pb2.Worker.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.InjectionStatus.FromString,
                )
        self.SetInjected = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/SetInjected',
                request_serializer=mitm__mapper_dot_mitm__mapper__pb2.InjectedRequest.SerializeToString,
                response_deserializer=shared_dot_Ack__pb2.Ack.FromString,
                )
        self.GetLastKnownLocation = channel.unary_unary(
                '/mapadroid.mitm_mapper.MitmMapper/GetLastKnownLocation',
                request_serializer=shared_dot_Worker__pb2.Worker.SerializeToString,
                response_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LastKnownLocationResponse.FromString,
                )


class MitmMapperServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLastPossiblyMoved(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLatest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestLatest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPokestopVisits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPokestopVisits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInjectionStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetInjected(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastKnownLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MitmMapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLastPossiblyMoved': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastPossiblyMoved,
                    request_deserializer=shared_dot_Worker__pb2.Worker.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.LastMoved.SerializeToString,
            ),
            'UpdateLatest': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateLatest,
                    request_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryUpdateRequest.FromString,
                    response_serializer=shared_dot_Ack__pb2.Ack.SerializeToString,
            ),
            'RequestLatest': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestLatest,
                    request_deserializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryRequest.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryResponse.SerializeToString,
            ),
            'SetLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLevel,
                    request_deserializer=mitm__mapper_dot_mitm__mapper__pb2.SetLevelRequest.FromString,
                    response_serializer=shared_dot_Ack__pb2.Ack.SerializeToString,
            ),
            'SetPokestopVisits': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPokestopVisits,
                    request_deserializer=mitm__mapper_dot_mitm__mapper__pb2.SetPokestopVisitsRequest.FromString,
                    response_serializer=shared_dot_Ack__pb2.Ack.SerializeToString,
            ),
            'GetPokestopVisits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPokestopVisits,
                    request_deserializer=shared_dot_Worker__pb2.Worker.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.PokestopVisitsResponse.SerializeToString,
            ),
            'GetLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLevel,
                    request_deserializer=shared_dot_Worker__pb2.Worker.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.LevelResponse.SerializeToString,
            ),
            'GetInjectionStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInjectionStatus,
                    request_deserializer=shared_dot_Worker__pb2.Worker.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.InjectionStatus.SerializeToString,
            ),
            'SetInjected': grpc.unary_unary_rpc_method_handler(
                    servicer.SetInjected,
                    request_deserializer=mitm__mapper_dot_mitm__mapper__pb2.InjectedRequest.FromString,
                    response_serializer=shared_dot_Ack__pb2.Ack.SerializeToString,
            ),
            'GetLastKnownLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastKnownLocation,
                    request_deserializer=shared_dot_Worker__pb2.Worker.FromString,
                    response_serializer=mitm__mapper_dot_mitm__mapper__pb2.LastKnownLocationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mapadroid.mitm_mapper.MitmMapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MitmMapper(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLastPossiblyMoved(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/GetLastPossiblyMoved',
            shared_dot_Worker__pb2.Worker.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.LastMoved.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateLatest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/UpdateLatest',
            mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryUpdateRequest.SerializeToString,
            shared_dot_Ack__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestLatest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/RequestLatest',
            mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryRequest.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.LatestMitmDataEntryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/SetLevel',
            mitm__mapper_dot_mitm__mapper__pb2.SetLevelRequest.SerializeToString,
            shared_dot_Ack__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPokestopVisits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/SetPokestopVisits',
            mitm__mapper_dot_mitm__mapper__pb2.SetPokestopVisitsRequest.SerializeToString,
            shared_dot_Ack__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPokestopVisits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/GetPokestopVisits',
            shared_dot_Worker__pb2.Worker.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.PokestopVisitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/GetLevel',
            shared_dot_Worker__pb2.Worker.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.LevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInjectionStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/GetInjectionStatus',
            shared_dot_Worker__pb2.Worker.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.InjectionStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetInjected(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/SetInjected',
            mitm__mapper_dot_mitm__mapper__pb2.InjectedRequest.SerializeToString,
            shared_dot_Ack__pb2.Ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastKnownLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapadroid.mitm_mapper.MitmMapper/GetLastKnownLocation',
            shared_dot_Worker__pb2.Worker.SerializeToString,
            mitm__mapper_dot_mitm__mapper__pb2.LastKnownLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
