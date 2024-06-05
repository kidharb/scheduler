import zmq
import os

context = zmq.Context()

ip = os.environ['ZMQ_SERVER_IP']
port = os.environ['ZMQ_SERVER_PORT']

print(ip)
print(port)
#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.PAIR)
socket.connect("tcp://" + ip + ":" + port)

for request in range(10):
    print("Sending request %s …" % request)
    bytes_val = request.to_bytes(1, 'big') 
    socket.send(bytes_val)
