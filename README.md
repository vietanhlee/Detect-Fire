# Nhận diện đám cháy và thông báo qua telegram

## Sơ qua dự án

Dự án sử dụng cấu trúc mạng `YOLO`, train tận dụng lại model pre-train `YOLO11s.pt` và bộ dataset về các đám lửa cháy đã được gán nhãn.

> Thông tin bộ dataset có thể được tải xuống ở [đây](https://www.mediafire.com/file/plf3h32g8q1tyik/firedata.zip/file). Nếu link hỏng có thể lấy ở mục `\Identify Fire\training\dataset`


## Demo kết quả
![](https://raw.githubusercontent.com/vietanhlee/Identify-Fire/refs/heads/main/display_github/demo%201.png)

<p align = 'center'> Khi phát hiện ra lửa</p>

![](https://raw.githubusercontent.com/vietanhlee/Identify-Fire/refs/heads/main/display_github/demo%202.png)

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

  - **B1**: thay dòng lệnh sau 
  ```python
    cam = cv2.VideoCapture(r'\Identify Fire\test.mp4)
  ``` 
  ở dòng 7 file `\Identify Fire\main.py` thành
  ``` python
    cam = cv2.VideoCapture(0)
  ```
  - **B2**: nhấn run để chạy.

## Tự train lại cho để model tốt hơn 

Model `best n.pt` trên được train dựa trên pre_train model `YOLO11n.py` với epochs là 200. Nếu cấu hình CPU khỏe có thể tự train lại bằng cách chạy file notebook: `\Identify Fire\training\main.ipynb` với số epochs lớn hơn 200. 

# Tích hợp báo cháy thông qua telegram

- Thay `api_key` và `id` của telegram vào 2 dòng này trong code ở file `main.py` để có thể báo về telegram của bạn

```python
  api_key = '7278180996:AAF3zjRmDm2tpTYzl5W1rRXMfTBkt47xWBA'
  id = '5510302349'
```
![](https://raw.githubusercontent.com/vietanhlee/Identify-Fire/refs/heads/main/display_github/tele.jpg)
<p align = 'center'> Thông báo qua telegram</p>
