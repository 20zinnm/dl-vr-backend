# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protocol_pb2 as protocol__pb2


class EvaluatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Evaluate = channel.unary_stream(
        '/dlvr.Evaluator/Evaluate',
        request_serializer=protocol__pb2.EvaluateRequest.SerializeToString,
        response_deserializer=protocol__pb2.ProgressUpdate.FromString,
        )


class EvaluatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Evaluate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EvaluatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Evaluate': grpc.unary_stream_rpc_method_handler(
          servicer.Evaluate,
          request_deserializer=protocol__pb2.EvaluateRequest.FromString,
          response_serializer=protocol__pb2.ProgressUpdate.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dlvr.Evaluator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
