from opcua import  Client

url = "opc.tcp://localhost:4840"

client = Client(url)

client.connect()

print("Client connected")

