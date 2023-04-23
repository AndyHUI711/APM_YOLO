from ultralytics import YOLO

# Load a model
model = YOLO('weights/yolov5su.pt')  # load a custom trained

# Export the model
model.export(format='engine',device=0)
