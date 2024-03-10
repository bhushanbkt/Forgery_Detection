import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
# Function to load the YOLO model
@st.cache(allow_output_mutation=True)
def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(model_path)
    return model

# Streamlit app
def main():
    st.title('YOLOv8 Object Detection App')

    # Sidebar for YOLO configuration
    conf = st.sidebar.slider("Confidence Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

    # Load the YOLO model
    model = load_model('best (8).pt')

    # File uploader
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", 'bmp', 'webp'])

    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform object detection when button is clicked
        if st.button('Execute'):
            # Run inference
            with st.spinner("Running inference..."):
                res = model.predict(image, conf=conf)

            # Plot the detected objects on the image
            # st.image(res[0].plot().numpy(), caption='Detected Image', use_column_width=True)
            st.image(res[0].plot(), caption='Detected Image', use_column_width=True)

            # Display detection results
            with st.expander("Detection Results"):
                for box in res[0].boxes:
                    st.write(box.xywh)

if __name__ == '__main__':
    main()
