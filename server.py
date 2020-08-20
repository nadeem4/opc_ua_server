import datetime
import time
from random import randint

from opcua import Server

server = Server()

# define opc ua url
url = "opc.tcp://localhost:4840"

# set the endpoint
server.set_endpoint(url)

# set the address space
name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

# get root node
node = server.get_objects_node()


param = node.add_object(addspace, "Parameters")

tempVar = param.add_variable(addspace, "Temperature", 0)
pressureVar = param.add_variable(addspace, "Pressure", 0)
timeVar = param.add_variable(addspace, "Time", 0)

tempVar.set_writable()
pressureVar.set_writable()
timeVar.set_writable()

server.start()

print("Server has started at {}".format(url))

while True:
    tempVal = randint(10, 50)
    pressureVal = randint(200, 999)
    timeVal = datetime.datetime.now()

    print("Temperature: {}, Pressure: {}, time: {}".format(tempVal, pressureVal, timeVal))

    tempVar.set_value(tempVal)
    pressureVar.set_value(pressureVal)
    timeVar.set_value(timeVal)

    time.sleep(2)
