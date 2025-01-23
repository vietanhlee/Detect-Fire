# Nhận diện đám cháy

## Sơ qua dự án

Dự án sử dụng cấu trúc mạng `YOLO`, train tận dụng lại model pre-train `YOLO11s.pt` và bộ dataset về các đám lửa cháy đã được gán nhãn.

> Thông tin bộ dataset có thể được tải xuống ở [đây](https://www.mediafire.com/file/plf3h32g8q1tyik/firedata.zip/file). Nếu link hỏng có thể lấy ở mục `\Identify Fire\training\dataset`


## Demo kết quả
![](https://raw.githubusercontent.com/vietanhlee/Identify-Fire/refs/heads/main/demo%201.png)

<p align = 'center'> Khi phát ra hiện </p>

![](https://raw.githubusercontent.com/vietanhlee/Identify-Fire/refs/heads/main/demo%202.png)

<p align = 'center'> Khi Không có lửa </p>

## Cách chạy

### Cài thư viện cần thiết:
- Mở terminal ở thư mục vừa clone và chạy đoạn lệnh sau:

    ``` bash
    pip install -r 'Identify Fire/requirements.txt' 
    ```

### Chạy thử code

- #### Chạy nhanh demo theo data video có sẳn:

    Chỉ cần chạy file  `\Identify Fire\main.py`

- #### Chạy theo camera local realtime:

  - B1: thay dòng lệnh sau 
  ```python
  cam = cv2.VideoCapture(r'\Identify Fire\test.mp4)
  ``` 
  ở dòng 7 file `\Identify Fire\main.py` thành
  ``` python
  cam = cv2.VideoCapture(0)
  ```

  - B2: nhấn run để chạy.'

## Tự train lại cho để model tốt hơn 

Model `best n.pt` trên được train dựa trên pre_train model `YOLO11n.py` với epochs là 200. Nếu cấu hình CPU khỏe có thể tự train lại bằng cách chạy file notebook: `\Identify Fire\training\main.ipynb` với số epochs lớn hơn 200. 