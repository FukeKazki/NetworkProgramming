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
sock.listen()
# 接続要求を受け入れる
sock_c, addr = sock.accept()

msg = "4432"

try:
    sock_c.sendall(msg.encode("UTF-8"))
except:
    print("sendall function failed.")

sock_c.close()
sock.close()