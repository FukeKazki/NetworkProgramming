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

BUFSIZE = 256 * 256

# ルールを受信
rule = sock.recv(BUFSIZE)
# 表示
print(rule.decode("UTF-8"))

# キーボードから入力した0~2の数字のどれかを送る
while True:
    # 入力
    inputNumber = input('数字を入力してください: ')
    # 送信
    sock.sendall(inputNumber.encode('UTF-8'))
    # 受信
    result = sock.recv(BUFSIZE)
    # 表示
    print(result.decode("UTF-8"))

    if inputNumber == '3':
        break

sock.close()