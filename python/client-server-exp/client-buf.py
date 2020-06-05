import socket
import signal
import time

# キーボードからの[ctrl]+[c]を非同期で受付
signal.signal(signal.SIGINT, signal.SIG_DFL)

# ソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 接続先
HOST = "127.0.0.1"
PORT = 50000

# 接続
sock.connect((HOST, PORT))

# 受信
BUFSIZE = 256

print("[sleep a little...]")
time.sleep(3)
print("[waked up!]")

data = sock.recv(BUFSIZE)
print("[received]")
print(data.decode("UTF-8"))


print("[sleep a little...]")
time.sleep(3)
print("[waked up!]")

data = sock.recv(BUFSIZE)
print("[received]")
print(data.decode("UTF-8"))

# ソケットを閉じる
sock.close()