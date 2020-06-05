import socket
import signal

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
data = sock.recv(BUFSIZE)

print(data.decode("UTF-8"))

# ソケットを閉じる
sock.close()