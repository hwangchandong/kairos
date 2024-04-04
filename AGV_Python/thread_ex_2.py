import threading
import time

def sum(name, value):
    for i in range (0, value):
        print(f"{name}: {i}")

#쓰레드의 문법임 
th1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
th2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))
#함수 하나로 쓰레드 두개 돌림 
th1.start()
th2.start()

print("main thread")

th1.join()
th2.join()
