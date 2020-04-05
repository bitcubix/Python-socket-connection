import socket

# define host and port
host = "<ip-address>"
port = 5000

server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# set number of max clients at the same time
server_socket.listen(2)
# accept new connection
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    # send message to the client
    conn.send(data.encode())

# close the connection
conn.close()
