import grpc
from concurrent.futures import ThreadPoolExecutor
import hello_world_pb2
import hello_world_pb2_grpc

class HelloWorldServicer(hello_world_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        return hello_world_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(ThreadPoolExecutor())
    hello_world_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
