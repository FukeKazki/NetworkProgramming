import socket
import signal
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

# 接続要求を受け入れる
while True:
    sock_c, addr = sock.accept()
    # メッセージの送信
    msg = "4432"
    try:
        sock_c.sendall(msg.encode("UTF-8"))
    except:
        print("sendall function failed.")
    # 通信用ソケットを閉じる
    sock_c.close()

# 待ち受けようソケットを閉じる
sock.close()