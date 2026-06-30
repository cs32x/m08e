### m08/guess-server0.py
import random
from socket32 import create_new_socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with create_new_socket() as s:
    # Bind socket to address and queue connection requests
    print("GUESS-THE-NUMBER server started. Listening on", (HOST, PORT))

    # Answer incoming connection
    print('Connected by', <client>)

    # Create a secret for this connection    
    secret = random.randint(1, 100)

    # Send and receive messages through the connection
    while True:   # message processing loop
        msg = # recv guess from client
        guess = int(msg)

        # Check guess against secret and respond
        if guess == secret:
            # sendall('Exactly! You win!')
        elif guess < secret:
            # sendall('Too small!')
        else:
            # sendall('Too big!')

    # If we get here, client broke connection
