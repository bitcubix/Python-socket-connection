import socket

# host and port same as server
host = "<ip-address>"
port = 5000

# initiate connection
client_socket = socket.socket()
# connect to the server
client_socket.connect((host, port))

# get input
message = input(' -> ')

while message.lower().strip() != 'bye':
    # send message to server
    client_socket.send(message.encode())
    # receive response from server
    data = client_socket.recv(1024).decode()

    # output response from server
    print(' <- ' + data)

    # get input again
    message = input(' -> ')

# close the connection
client_socket.close()
