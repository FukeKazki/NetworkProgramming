import socket
import signal

MY_ADDRESS = ''
MY_PORT = 50000

BUFSIZE = 1024
WAIT_TIME = 1
# AF_INET: ipv4
# SOCK_STREAM: TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((MY_ADDRESS, MY_PORT))

sock.listen()
# HTTP Responce
statusline = 'HTTP/1.1 200 OK\r\n'
brankline = '\r\n'
contents = '<!DOCTYPE html><html><head><meta charset=`utf-8`/><title>いいよおおお</title></head><body>いいよ〜</body></html>'

def recv_crlf(sock_c):
    BUFSIZE_CRLF = 1
    req = ''

    while req.find('\r\n') < 0:
        data = sock_c.recv(BUFSIZE_CRLF)
        if not data:
            break
        req += data.decode('UTF-8')

    if req.find('\r\n') < 0:
        return None

    return req[:-2]

def get_request(sock_c):
    sock_c.settimeout(WAIT_TIME)
    try:
        req_l = recv_crlf(sock_c)
        req_h = {} 
        req_m = ''

        pair = recv_crlf(sock_c)

        while pair != None and pair != '':
            k, v = pair.split(': ')
            req_h[k] = v
            pair = recv_crlf(sock_c)
        
        if 'Content-Length' in req_h:
            req_m = sock_c.recv(BUFSIZE).decode('UTF-8')
            while len(req_m) < int(req_h['Content-Length']):
                data = sock.recv(BUFSIZE)
                if not data:
                    break
                req_m += data.decode('UTF-8')

        return (req_l, req_h, req_m)
    except:
        return (None, None, None)


while True:
    sock_c, addr = sock.accept()

    line, header, body = get_request(sock_c)

    print('request line: {}\n'.format(line))
    print('request header: {}\n'.format(header))
    print('request body: {}\n'.format(body))

    sock_c.close()

sock.close()


