import socket
import signal
import multiprocessing
# キーボードからの[ctrl]+[c]を非同期で受付
signal.signal(signal.SIGINT, signal.SIG_DFL)

rule = 'ルールです'

def jGame(sock_c, addr):
    try:
        sock_c.sendall(rule.encode('UTF-8'))
    except:
        print('sendall function failed.')
    
    while True:
        data = sock_c.recv(BUFSIZE)
        print(data.decode('UTF-8'))

MY_ADDRESS = ''
MY_PORT = 50000
BUFSIZE = 256

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((MY_ADDRESS, MY_PORT))
    sock.listen()

    # 接続要求を受け入れる
    while True:
        sock_c, addr = sock.accept()

        p = multiprocessing.Process(target=jGame, args=(sock_c, addr))
        p.start()
    

# 待ち受けようソケットを閉じる
sock.close()