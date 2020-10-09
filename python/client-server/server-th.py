import socket
import signal
import threading
# キーボードからの[ctrl]+[c]を非同期で受付
signal.signal(signal.SIGINT, signal.SIG_DFL)

# socket object
# 第一引数: Address Family => IPv4
# 第二引数: Socket Type => TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# taple型 (IPアドレス, ポート番号)
sock.bind(("", 50000))
# ソケットを待ち状態にする
sock.listen()

BUFSIZE = 256

def communication(sock_c, addr):
    msg = 'hello!'
    try:
        sock_c.sendall(msg.encode('UTF-8'))
    except:
        print('sendall function failed.')

    data = sock_c.recv(BUFSIZE)
    print(data.decode('UTF-8'))

# 接続要求を受け入れる
while True:
    sock_c, addr = sock.accept()

    p = threading.Thread(target=communication, args=(sock_c, addr))
    p.start()
    

# 待ち受けようソケットを閉じる
sock.close()