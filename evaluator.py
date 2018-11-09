import evaluator_pb2
import evaluator_pb2_grpc

class Evaluator(evaluator_pb2_grpc.EvaluatorServicer):
    def Evaluate(self, request, context):
        # build Keras model
        for layer in request.layers:
            layer = protocol_pb2.Layer(layer)
            typ = request.WhichOneof("definition")
            if (typ == None):
                continue

            if (typ == "convolution"):
                # do something here
                conv = layer.convolution
                # conv.filters
            elif (typ == "dropout"):
                # do something here
            elif (typ == "flatten"):
                

        # train the model

        # send progress updates
        # yield evaluator_pb2_grpc.ProgressUpdate(accuracy = 1)