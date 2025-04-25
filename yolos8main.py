from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# Load a model


model = YOLO('model/yolov8s.pt').load('yolov8n.pt') # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='yolo8s.yaml', epochs=1,cache=False,exist_ok=True)