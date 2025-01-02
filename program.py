#   Chat Program
#   Here is the gist of what this program does:
#   - Connects to another user(with different port number) utilizing sockets and threads
#   - Utilizes threading to enter in a loop of reading and writing message
#   - These reading and writing thread between two user programs allows for chatting through sockets


import socket
import threading
import time

class ChatUser:
    # Initializing function
    def __init__(self, host='localhost'):
        self.host = host
        self.server_port = int(input("Enter the server port number of this user: "))
        self.server_socket = None
        self.client_socket = None
        self.connection_socket = None  

    # Start server funtion
    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.server_port))
        self.server_socket.listen(5)
        self.connection_socket, addr = self.server_socket.accept()
        # Read messages from this socket
        self.receive_messages()

    # Receive message function
    def receive_messages(self):
        try:
            while True:
                message = self.connection_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received message : {message}")
                else:
                    break
        except Exception as e:
            print(f"Error receiving message: {e}")
        finally:
            self.connection_socket.close()

    def start_client(self):
        print(f"Chat server created : {self.server_port}")
        client_port = int(input('Enter the port number to connect to : '))
        time.sleep(5)  # Delay to allow other user to connect
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, client_port))
            print(f"Connected to server on :{client_port}")
            # Writing thread for sending messages
            send_thread = threading.Thread(target=self.send_messages)
            send_thread.start()
        except Exception as e:
            print(f"Client error: {e}")

    # Send messages function
    def send_messages(self):
        try:
            while True:
                message = input("")
                if message.lower() == "exit":
                    print("Exiting..")
                    break
                if self.client_socket:
                    self.client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
        finally:
            self.close_connections()

    def close_connections(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        if self.connection_socket:
            self.connection_socket.close()

if __name__ == "__main__":
    user = ChatUser()
    server_thread = threading.Thread(target=user.start_server)
    server_thread.start()
    user.start_client()
