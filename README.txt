Implementation of a Chat Program


Description: 
This project implements a simple chat program. The program contains two files- user1.py and user2.py. Both the files create two threads: a main(reading) thread and a writing thread. Here is the brief description of what the program does:

- Creates a new thread and takes as an input the port number of another user
- Connects to user using sockets and enters in a loop of reading and writing message
- Creates another thread called ServerSocket and listens on the socket for connection
- The created thread will attempt to read messages from connection socket and print to the screen
- These reading and writing thread between two user programs allows for chatting through sockets

Programming Environment:
This source code for this program is written in Python in Visual Studio Code.