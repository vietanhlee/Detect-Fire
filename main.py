from ultralytics import YOLO
import cv2

model = YOLO(r'\Identify Fire\best n.pt')

cam = cv2.VideoCapture(0)

while True:
    check, cap = cam.read()
    cap = cv2.flip(cap, 1)

    if not check:
        print("Không thể đọc từ camera.")
        break
    
    res = model.predict(source= cap, conf = 0.3, verbose= False)
    res = res[0]
    cls = res.boxes.cls
    conf = res.boxes.conf

    boxes = res.boxes.xyxy

    for i in range(len(boxes)):
        if(cls[i] == 0):
            x1, y1, x2, y2 = map(int, boxes[i])

            cv2.rectangle(cap, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                    cap,
                    f'{round(float(conf[i]), 2)}', 
                    (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2
                )
            
            x, y = (x1 + x2) //2, (y1 + y2) // 2 
            color = (0, 255, 0)             
            cv2.circle(cap, (x, y), radius=3, color=color, thickness=-1)  # thickness=-1 để tô đầy hình tròn
    
    fire = len(boxes)
    if(fire != 0):
        cv2.putText(cap, f'{fire} fire detected', (30, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2
                )
    else:
        cv2.putText(cap, f'No fire visible in the observation area', (30, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
                )
    cv2.imshow('app', cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()