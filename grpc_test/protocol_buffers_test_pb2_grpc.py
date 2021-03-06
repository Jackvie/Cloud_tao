# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protocol_buffers_test_pb2 as protocol__buffers__test__pb2


class HelloServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/HelloService/SayHello',
        request_serializer=protocol__buffers__test__pb2.Request.SerializeToString,
        response_deserializer=protocol__buffers__test__pb2.Response.FromString,
        )


class HelloServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=protocol__buffers__test__pb2.Request.FromString,
          response_serializer=protocol__buffers__test__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HelloService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
