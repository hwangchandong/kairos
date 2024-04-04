import cv2
import mediapipe as mp
import numpy as np
import threading
import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)  # 아두이노와의 연결을 위한 대기 시간

#아두이노 거리값 보내기
def led2Ardu(led_brightness):
    led_v = 'b'+str(led_brightness)+'s'
    ser.write(led_v.encode('utf-8'))

# a-b 사이의 유클리드 거리 구하기
def get_distance(ax, ay, bx, by):
    a = np.array([ax, ay])
    b = np.array([bx, by])

    distance = np.sqrt(np.sum(np.square(a - b))) # 넘파이의 배열 제곱 np.square(arr) 
    # 최소 거리 갱신   
    distance = 0 if distance < 10 else distance
    return distance



mp_hands = mp.solutions.hands  # 손 인식 모델
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils  # 랜드마크를 그릴 때 사용할 유틸 함수

# 이미지 한편에 넣을 슬라이드 바 세팅값
bar_x, bar_y, bar_width, bar_height = 500, 50, 20, 255
bar_max_color = (0, 255, 0)
max_distance = 200    # 거리를 LED 밝기로 변환할 때 최대 거리값
led_bright_max = 255  # LED 최대 밝기

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)  # RGB 이미지에서 손 찾고 랜드마크 추출한 결과 반환

    if results.multi_hand_landmarks:
        # 손, 엄지, 검지 랜드마크 저장
        hand_landmarks = results.multi_hand_landmarks[0]
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

        img_height, img_width, _ = frame.shape
        # 엄지, 검지 랜드마크 좌표를 이미지에 맞춰 조정
        thumb_x, thumb_y = int(thumb_tip.x * img_width), int(thumb_tip.y * img_height)
        index_x, index_y = int(index_tip.x * img_width), int(index_tip.y * img_height)

        # 엄지-검지 거리값!!
        distance = get_distance(thumb_x, thumb_y, index_x, index_y)
        # print("Dist: " + f"{distance}")
        # time.sleep(0.2)
    
        # 거리를 LED 밝기로 변환하기
        led_brightness = int((distance / max_distance) * led_bright_max)
        # print("Bright: " + f"{led_brightness}")
        # time.sleep(0.2)

        #쓰레딩 시작
        th1 = threading.Thread(target=led2Ardu, args=(led_brightness))
        th1.start()

        # 스케일 바 색상 (bar_max_color = (0, 255, 0))
        bar_color = tuple(np.multiply(bar_max_color, led_brightness / led_bright_max).astype(int))

        # 밝기 수치를 슬라이드 바로 시각화 하기  
        # 슬라이드바 좌특상단, 우측하단, 흰색, 채우기 
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), -1)  
        # 바 내부 채우기
        cv2.rectangle(frame, (bar_x, bar_y + bar_height - led_brightness), (bar_x + bar_width, bar_y + bar_height), tuple(map(int, bar_color)), -1)  

        # 엄지와 검지에 그린 동그라미 표시하기
        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)  #  
        cv2.circle(frame, (index_x, index_y), 5, (0, 255, 0), -1)  #  

    cv2.imshow('Hand Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
