import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="SkyScan AI", page_icon="👁️")

st.title("👁️ SkyScan: AI Object Detection")
st.markdown("Upload a photo (aerial, street, or construction site) to detect objects.")

# 1. Load the Model
# This downloads 'yolov8n.pt' automatically on the first run.
# It is the smallest, fastest model.
try:
    model = YOLO('yolov8n.pt')
except Exception as e:
    st.error(f"Error loading model: {e}")

# 2. Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Convert the file to an image object
    image = Image.open(uploaded_file)
    
    # Display the original
    st.image(image, caption="Original Image", use_container_width=True)
    
    if st.button("Detect Objects 🔍"):
        with st.spinner("Analyzing image..."):
            # 3. Run Inference
            results = model(image)
            
            # 4. Plot Results
            # results[0].plot() returns a numpy array with boxes drawn on it
            # We need to reverse the colors because OpenCV uses BGR, but PIL uses RGB
            res_plotted = results[0].plot()[:, :, ::-1]
            
            # Convert back to a displayable image
            res_image = Image.fromarray(res_plotted)
            
            st.success("Scan Complete!")
            st.image(res_image, caption="AI Analysis Result", use_container_width=True)
            
            # Optional: Show what it found
            # st.write(results[0].verbose())