from ultralytics import YOLO
import cv2
import requests
import datetime
import threading


# Load model tốt nhất đã được train
model = YOLO(r'model.pt')

# Khởi tạo camera, 0 mặc định là camera ở local
cam = cv2.VideoCapture(r'test.mp4')

api_key = '7278180996:AAF3zjRmDm2tpTYzl5W1rRXMfTBkt47xWBA'
id = '5510302349'

chat = f'Có cháy lúc {datetime.datetime.now().time()}'
url = f'https://api.telegram.org/bot{api_key}/sendMessage?chat_id={id}&text={chat}'
def send_telegram_message():
    requests.get(url)

while True:
    # Đọc ảnh
    check, cap = cam.read()
    # cap = cv2.flip(cap, 1)
    if not check:
        print("Không thể đọc từ camera.")
        break
    
    # Dự đoán 
    res = model.predict(source= cap, conf = 0.4, verbose= False) # verbose = False để tắt các dòng thông báo thừa

    # Lấy ra độ tin cậy của từng box
    conf = res[0].boxes.conf
    # Lấy ra data về các box
    boxes = res[0].boxes.xyxy

    # Vẽ và hiển thị thông qua cv2
    for i in range(len(boxes)):
        # Ép kiểu về số nguyên do yêu cầu thông số của cv2 qui định
        x1, y1, x2, y2 = map(int, boxes[i]) # Lấy tọa độ box
        # Vẽ box
        cv2.rectangle(cap, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # Điền độ tin cậy của box
        cv2.putText(cap, f'{round(float(conf[i]), 2)}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # vẽ tâm box
        x, y = (x1 + x2) //2, (y1 + y2) // 2 
        color = (0, 255, 0)             
        cv2.circle(cap, (x, y), radius=3, color=color, thickness=-1)  # thickness=-1 để tô đầy hình tròn
    
    # Thông báo về số ngọn lửa được tìm thấy
    fire = len(boxes)
    if(fire != 0):
        # Ghi lên màn
        cv2.putText(cap, f'{fire} fire detected', (30, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    else:
        cv2.putText(cap, f'No fire visible in the observation area', (30, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        if(api_key != None):
            # Thông báo qua luồng riêng biệt để tránh delay trong vòng lặp
            threading.Thread(target=send_telegram_message, daemon=True).start()
    # Hiển thị ra màn hình
    cv2.imshow('fire', cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Giải phóng camera
cam.release()
cv2.destroyAllWindows()