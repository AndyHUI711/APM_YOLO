# APM_YOLO

Test Results:\
Using Ubuntu 20.04, Python-3.7.13 torch-1.12.1 CUDA:0 (NVIDIA GeForce RTX 2060 with Max-Q Design, 5918MiB) \
Test Video 248 frame, FPS = 1/(TOTAL PROCESS TIME)

## YOLOV5u FAMILY
### yolov5mu_engine_osnet_x1_0_imagenet:
Speed: 0.6ms pre-process, 16.6ms inference, 1.8ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 19.2ms FPS 52.1\
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233098974-5de3924b-55eb-4e59-a977-e7e44e535df7.jpg)

### yolov5su_engine_osnet_x1_0_imagenet2:
Speed: 0.7ms pre-process, 7.0ms inference, 2.0ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 9.9ms FPS 101.0\
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233100402-d526ac68-64a3-4fc4-b429-2b9dee2a06c8.jpg)

### yolov5nu_engine_osnet_x1_0_imagenet:
Speed: 0.7ms pre-process, 3.6ms inference, 1.4ms NMS, 0.1ms bytetrack update per image at shape (1, 3, 640, 640) Total 5.8ms FPS 172.4\
![2 mp4-frame-234](https://user-images.githubusercontent.com/82593344/233101246-7b33b64f-c559-4a11-8752-b1585d19bca2.jpg)

### yolov5mu_pt_osnet_x1_0_imagenet:
Speed: 0.4ms pre-process, 14.5ms inference, 1.7ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 16.8ms FPS 59.5\
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233101864-a4ee39ae-aea5-479a-8c14-bcfc6b2ea2ae.jpg)

### yolov5su_pt_osnet_x1_0_imagenet:
Speed: 0.4ms pre-process, 6.6ms inference, 2.0ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 9.2ms FPS 108.7\
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233102095-a3649aae-770a-45f0-b164-ce64f1a321b6.jpg)

### yolov5nu_pt_osnet_x1_0_imagenet:
Speed: 0.4ms pre-process, 4.6ms inference, 0.6ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 5.8ms FPS 172.4\
![2 mp4-frame-234](https://user-images.githubusercontent.com/82593344/233102323-5c5569c1-e97c-4efc-8b31-5eaafa35db53.jpg)

## YOLOV8 FAMILY
### yolov8m_engine_osnet_x1_0_imagenet2
Speed: 0.6ms pre-process, 19.0ms inference, 1.6ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 21.4ms FPS 46.7\
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233103622-8f16458a-c1e9-4ac2-8fbd-e1a8ac056382.jpg)

### yolov8s_engine_osnet_x1_0_imagenet2
Speed: 0.6ms pre-process, 8.4ms inference, 1.6ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 11ms FPS 90.9\ 
![2 mp4-frame-232](https://user-images.githubusercontent.com/82593344/233104906-65e57dba-59cb-45bb-a79a-e8e01472fa33.jpg)


### yolov8n_engine_osnet_x1_0_imagenet2
Speed: 0.6ms pre-process, 3.7ms inference, 1.3ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 5.8ms FPS 172.4\ 
![2 mp4-frame-234](https://user-images.githubusercontent.com/82593344/233104035-d203e8c7-281a-4f71-9d4d-070bf54a1247.jpg)

### yolov8m_pt_osnet_x1_0_imagenet
Speed: 0.4ms pre-process, 14.9ms inference, 1.2ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 16.7ms FPS 59.9\ 
![2 mp4-frame-235](https://user-images.githubusercontent.com/82593344/233103799-d440454e-7a7c-4788-8448-271d56516951.jpg)
### yolov8s_pt_osnet_x1_0_imagenet
Speed: 0.4ms pre-process, 7.7ms inference, 1.5ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 9.8.ms FPS 102.0\  
![2 mp4-frame-232](https://user-images.githubusercontent.com/82593344/233105038-c22811a0-6edf-4b39-8f57-4b01ef107b38.jpg)

### yolov8n_pt_osnet_x1_0_imagenet
Speed: 0.5ms pre-process, 3.9ms inference, 1.1ms NMS, 0.2ms bytetrack update per image at shape (1, 3, 640, 640) Total 5.7ms FPS 175.4\ 
![2 mp4-frame-234](https://user-images.githubusercontent.com/82593344/233104245-b05c3eed-fe32-4383-be12-92c7afbb1f68.jpg)






