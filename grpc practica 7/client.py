import grpc
import shop_pb2
import shop_pb2_grpc

def run():
    # Establece la conexión al servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        # Crea un cliente para el servicio Shop
        stub = shop_pb2_grpc.ShopServiceStub(channel)
        
        # Ejemplo de llamada al método PurchaseItem
        purchase_request = shop_pb2.PurchaseRequest(product_id="123", quantity=2)
        purchase_response = stub.PurchaseItem(purchase_request)
        print("Respuesta de Compra de Artículo:", purchase_response.message)
        print("Total Price:", purchase_response.total_price)
        
        # Ejemplo de llamada al método MakePayment
        payment_request = shop_pb2.PaymentRequest(payment_method="credit_card", amount=20.0)
        payment_response = stub.MakePayment(payment_request)
        print("Respuesta de Pago:", payment_response.message)
        print("Éxito del Pago:", payment_response.success)

        # Ejemplo de llamada al método PlaceOrder
        order_request = shop_pb2.OrderRequest()
        order_request.items.extend([
            shop_pb2.PurchaseRequest(product_id="456", quantity=3),
            shop_pb2.PurchaseRequest(product_id="789", quantity=1)
        ])
        order_response = stub.PlaceOrder(order_request)
        print("Respuesta de Realización de Pedido:", order_response.order_id)
        for purchase in order_response.purchases:
            print("Artículo:", purchase.message)
            print("Precio Total:", purchase.total_price)

if __name__ == '__main__':
    run()
