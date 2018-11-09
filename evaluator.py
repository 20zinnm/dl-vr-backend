import evaluator_pb2
import evaluator_pb2_grpc
import grpc

class Evaluator(protocol_pb2_grpc.EvaluatorService):
    def Evaluate(self, request, context):
        # build Keras model
        for layer in request.layers:
            layer = protocol_pb2.Layer()
            typ = request.WhichOneof("definition")
            if (typ == None):
                continue
            if (typ == "convolution"):
                # do something here
                conv = layer.convolution
                # conv.filters

        # train the model

        # send progress updates
        # yield protocol_pb2.ProgressUpdate(accuracy = 1)
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    evaluator_pb2_grpc.add_EvaluatorServicer_to_server(Evaluator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()