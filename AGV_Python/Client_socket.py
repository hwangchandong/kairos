#client
import socket

HOST = "172.30.1.96" #서버의 IP
PORT = 9970

#1. 소켓 생성
# 주소체계 : Address Family INET (IPv4 프로토콜)
# Soc kind TCP Stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#3. 접속 시도
sock.connect((HOST,PORT))

#5. 데이터 송/수신
sock.sendall(bytes("Hello", "utf-8"))

#6. 접속 종료
sock.close()



