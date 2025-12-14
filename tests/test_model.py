import numpy as np
from ultralytics import YOLO

def test_model_loading():
    """Check if the model loads without crashing."""
    try:
        model = YOLO('yolov8n.pt')
        assert model is not None
        print("✅ Model loaded successfully")
    except Exception as e:
        assert False, f"Model failed to load: {e}"

def test_inference_dry_run():
    """Check if the model can process a blank image (sanity check)."""
    model = YOLO('yolov8n.pt')
    
    # Create a blank black image (640x640 pixels, 3 channels)
    dummy_image = np.zeros((640, 640, 3), dtype=np.uint8)
    
    # Run inference
    results = model(dummy_image)
    
    # Ensure we got a result object back
    assert len(results) > 0
    print("✅ Inference ran successfully on dummy data")