from ultralytics import YOLO
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import os
from ultralytics.engine.trainer import BaseTrainer
from ultralytics.data.converter import convert_coco
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import shutil

class yolo_class(Dataset):
    def __init__(self,model_yaml_path,yaml_path,model_pt_path):
        self.model_yaml_path=model_yaml_path
        self.yaml_path=yaml_path
        self.model_pt_path=model_pt_path
        self.model=YOLO(model_yaml_path).load(model_pt_path)
        self.root_path=None
    def trian_start(self,epochs=10):
        self.model.train(data=self.yaml_path, epochs=epochs,cache=False,exist_ok=True,resume=True)
    def predict_one_start(self,jpg_path):
        result=self.model.predict(jpg_path,save=True,conf=0.8)
        return result
    def val_start(self,epochs):
        result=self.model.val(data=self.yaml_path,plots=True,conf=0.00001)
        return result
    def export_start(self,model):
        self.model.export(format=model)
        