import socket


def create_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
            try:
                serversocket.bind((socket.gethostname(), 9000))
                serversocket.listen(5)

                while True:
                    (client_socket, address) =  serversocket.accept()

                    """ r_data = clientsocket.recv(5000).decode()
                    pieces = r_data.split("\n")
                    if len(pieces) >0: print(pieces[0]) """
                    print(f"\nConnected by {client_socket}\n")

                    response_body = [
                        '<html><body><h1>Hello, world!</h1>',
                    ]

                    response_body.append('</ul></body></html>')
                    response_body_raw = ''.join(response_body)
                    print(response_body_raw)

                    response_headers = {
                        'Content-Type': 'text/html; encoding=utf8',
                        'Content-Length': len(response_body_raw),
                        'Connection': 'close',
                    }

               

                    # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
                    response_proto = 'HTTP/1.1'
                    response_status = '200'
                    response_status_text = 'OK' # this can be random

                    client_socket.send(b'%s %s %s' % (response_proto, response_status, \
                                                        response_status_text))
                    client_socket.send(b'\n') # to separate headers from body
                    client_socket.send(bytes(response_body_raw))

                    client_socket.close()
            except KeyboardInterrupt:
                print("\n Shutting down..\n")
    except Exception as exc:
        print("Error:\n")
        print(str(exc))








if __name__ == "__main__":
    print(f"Server is running at: http://{socket.gethostname()}:9000")
    create_server()