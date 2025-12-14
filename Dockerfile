# 1. Use Python 3.10 slim (smaller base image)
FROM python:3.10-slim

# 2. Install system dependencies required for OpenCV/Computer Vision
# libglib2.0-0 and libgl1 are essential for image processing logic
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# 3. Set work directory
WORKDIR /app

# 4. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the app code AND the model file
# (This ensures the container works offline and doesn't download the model every time)
COPY . .

# 6. Expose Streamlit port
EXPOSE 8501

# 7. Run the app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=localhost"]