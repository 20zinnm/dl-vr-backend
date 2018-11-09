import protocol_pb2_grpc as evaluator_service;
import protocol_pb2 as evaluator_messages;

class EvaluatorService(evaluator_service.EvaluatorService):
    def Evaluate(self, request, context):
        