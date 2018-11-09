import protocol_pb2_grpc;
import protocol_pb2;

class EvaluatorService(protocol_pb2_grpc.EvaluatorService):
    def Evaluate(self, request, context):
        # build Keras model
        for layer in request.layers:
            layer = protocol_pb2.Layer()
        
        # train the model

        # send progress updates
        yield protocol_pb2.ProgressUpdate(accuracy = 1);
        