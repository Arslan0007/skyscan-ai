# 👁️ SkyScan AI

[![Live App](https://img.shields.io/badge/Demo-Live%20App-brightgreen?style=for-the-badge&logo=streamlit)](https://skyscan-ai.onrender.com)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![AI](https://img.shields.io/badge/Model-YOLOv8-green)

**SkyScan** is a computer vision application that detects objects in images using state-of-the-art AI. Built with the **YOLOv8** model and **Streamlit**, it provides real-time object detection capable of identifying cars, people, and infrastructure in aerial or ground-level photos.

## 🌟 Features
* **AI-Powered Detection:** Uses Ultralytics YOLOv8 (Nano) for fast, accurate inference.
* **Dockerized:** Fully containerized environment with pre-installed system dependencies (OpenGL/GLib).
* **Interactive UI:** Drag-and-drop interface powered by Streamlit.

## 🚀 Quick Start

### Option A: Run with Docker (Recommended)
This is the easiest way to run the app without worrying about installing PyTorch or OpenCV drivers locally.

1.  **Build the Image**
    ```bash
    docker build -t skyscan .
    ```

2.  **Run the Container**
    ```bash
    docker run -p 8501:8501 skyscan
    ```
    *Access the app at [http://localhost:8501](http://localhost:8501)*

### Option B: Run Locally (Python)

1.  **Create venv and install dependencies**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

2.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 🛠️ Tech Stack
* **Core:** Python 3.10
* **AI Model:** YOLOv8n (Nano)
* **Vision Library:** OpenCV (Headless)
* **Containerization:** Docker (Debian Bookworm)

---
*Built as part of the DevOps Journey 2025 Portfolio.*