# YOLOv8 目标检测项目

这是一个面向YOLO初学者的目标检测基础项目，基于Ultralytics YOLOv8实现。

## 🚀 快速开始

### 安装依赖
```bash
pip install ultralytics


使用方式：python yolos8main.py

文件结构
YOLO_ROOT/
├── annotations/               # 数据集目录
│   ├── images/         # 待检测图片
│   └── output/         # 检测结果（自动生成）
├── models/             # 自定义模型
├── run/                # 运行过程
└── yolos8main.py       # 主程序入口