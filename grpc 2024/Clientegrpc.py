import grpc
import hello_world_pb2
import hello_world_pb2_grpc

def run_client(name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_world_pb2_grpc.HelloWorldStub(channel)
    response = stub.SayHello(hello_world_pb2.HelloRequest(name=name))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run_client("Client 1")
    run_client("Client 2")
