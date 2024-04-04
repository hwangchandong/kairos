#server
import socket

HOST = "172.30.1.96"
PORT = 9970

#1. 서버 소켓생성 (접속 대기용 소켓)
# 주소체계 : Address Family INET (IPv4 프로토콜)
# Soc kind TCP Stream
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. 바인딩 (서버의 IP, 포트) 자기 자신이므로 ""로 해도 됨.
sock.bind(("", PORT))

#3. 접속 대기 (클라에게 귀를 기울임)
sock.listen()
print("Server is listening.")

#4. 클라 접속 수락 (실제 데이터 송수신 소켓)
c_sock, addr = sock.accept()
print(f"Connected to {addr}")

# 5. 데이터 수신 (최대 1024 비트)
read_data = c_sock.recv(1024)
print(f"Rx: {read_data.decode('utf-8')}")

#6. 접속 종료
c_sock.close() #클라
sock.close()   #서버