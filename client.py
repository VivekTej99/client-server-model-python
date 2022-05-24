
try:
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        hostname = "data.pr4e.org"
        PORT = 80
        sock.connect((hostname,PORT))
        CMD = "GET http://data.pr4e.org/page1.htm HTTP/1.0 \r\n\r\n".encode()
        sock.send(CMD) 

        while True:
            data = sock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end=' ')

except Exception as e:
    print(str(e))
    