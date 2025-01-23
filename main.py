from ultralytics import YOLO
import cv2
# Load model tốt nhất đã được train
model = YOLO(r'\Identify Fire\best n.pt')
# Khởi tạo camera, 0 mặc định là camera ở local

cam = cv2.VideoCapture(r'\Identify Fire\test.mp4')

while True:
    # Đọc ảnh
    check, cap = cam.read()
    cap = cv2.flip(cap, 1)

    if not check:
        print("Không thể đọc từ camera.")
        break
    
    # Dự đoán 
    res = model.predict(source= cap, conf = 0.2, verbose= False) # verbose = False để tắt các dòng thông báo thừa
    res = res[0] 
    cls = res.boxes.cls
    # Lấy ra độ tin cậy của từng box
    conf = res.boxes.conf
    # Lấy ra data về các box
    boxes = res.boxes.xyxy

    # Vẽ và hiển thị thông qua cv2
    for i in range(len(boxes)):
        if(cls[i] == 0):
            # Ép kiểu về số nguyên do yêu cầu thông số của cv2 qui định
            x1, y1, x2, y2 = map(int, boxes[i])

            # Vẽ box
            cv2.rectangle(cap, (x1, y1), (x2, y2), (0, 0, 255), 2)
            # Điền độ tin cậy của box
            cv2.putText(
                    cap,
                    f'{round(float(conf[i]), 2)}', 
                    (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2
                )
            
            # vẽ tâm box
            x, y = (x1 + x2) //2, (y1 + y2) // 2 
            color = (0, 255, 0)             
            cv2.circle(cap, (x, y), radius=3, color=color, thickness=-1)  # thickness=-1 để tô đầy hình tròn
    
    # Thông báo về số ngọn lửa được tìm thấy
    fire = len(boxes)
    if(fire != 0):
        cv2.putText(cap, f'{fire} fire detected', (30, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2
                )
    else:
        cv2.putText(cap, f'No fire visible in the observation area', (30, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
                )
    # Hiển thị ra màn hình
    cv2.imshow('app', cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera
cam.release()
cv2.destroyAllWindows()