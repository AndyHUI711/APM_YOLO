# Jetson Nano Python-3.6.9 torch-1.10.0a0+git36449ea CUDA:0 (NVIDIA Tegra X1, 3956MiB)
## Jetpack 4.6.3 TensorRT: 8.2.1.8
\
## YOLO V8 FAMILY' Half = False
### yolov8m_pt_osnet_x1_0_imagenet:
Speed: 10.9ms pre-process, 320.5ms inference, 19.3ms NMS, 1.8ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 352.5ms FPS 2.84

### yolov8s_pt_osnet_x1_0_imagenet:
Speed: 3.7ms pre-process, 137.0ms inference, 13.1ms NMS, 2.3ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 156.1ms FPS 6.41

### yolov8n_pt_osnet_x1_0_imagenet:
Speed: 2.9ms pre-process, 63.9ms inference, 7.4ms NMS, 1.7ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 75.9ms  FPS 13.18

### yolov8m_engine_osnet_x1_0_imagenet:
Speed: 33.5ms pre-process, 417.1ms inference, 30.5ms NMS, 2.2ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 483.3ms FPS 2.07

### yolov8s_engine_osnet_x1_0_imagenet:
Speed: 5.4ms pre-process, 172.1ms inference, 12.1ms NMS, 2.5ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 192.1ms FPS 5.21


### yolov8n_engine_osnet_x1_0_imagenet:
Speed: 5.7ms pre-process, 74.8ms inference, 7.0ms NMS, 1.5ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 89ms FPS 11.24

# -----------------------------------
## YOLOV5 FAMILY
### yolov5mu_pt_osnet_x1_0_imagenet
Speed: 4.0ms pre-process, 289.0ms inference, 16.7ms NMS, 2.0ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 311.7ms FPS 3.21

### yolov5su_pt_osnet_x1_0_imagenet
Speed: 4.6ms pre-process, 129.7ms inference, 14.6ms NMS, 1.9ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 150.8ms FPS 6.63

### yolov5nu_pt_osnet_x1_0_imagenet
Speed: 3.9ms pre-process, 61.2ms inference, 6.9ms NMS, 1.4ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 73.4ms FPS 13.62

### ImportError: /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block
### export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
### source ~/.bashrc
### yolov5mu_engine_osnet_x1_0_imagenet
Speed: 19.2ms pre-process, 367.2ms inference, 42.1ms NMS, 2.1ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 430.6ms FPS 2.32


### yolov5su_engine_osnet_x1_0_imagenet
Speed: 7.5ms pre-process, 152.9ms inference, 23.0ms NMS, 3.6ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 187ms FPS 5.35

### yolov5nu_engine_osnet_x1_0_imagenet
Speed: 4.5ms pre-process, 74.4ms inference, 8.1ms NMS, 1.6ms bytetrack update per image at shape (1, 3, 640, 640)\
Total 88.6ms FPS 11.29







