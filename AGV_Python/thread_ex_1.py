import threading
import time

def thread_1():
    while True:
        print("쓰레드 1")
        time.sleep(1.0)

# th1 = threading.Thread(target=thread_1)
th1 = threading.Thread(target=thread_1, daemon = True)
#th1.daemon = True  # 메인이 끝나면 같이 종료
th1.start()

# while True:
#     print("메인 쓰레드")
#     time.sleep(2.0)

i = 0
while (i <10 ):
    print("메인 쓰레드")
    time.sleep(2.0)
    i += 1