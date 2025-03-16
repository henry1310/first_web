import streamlit as st
import numpy as np
import cv2
from PIL import Image
img_file_buffer = st.camera_input('Take a picture')
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h,w,_ = img.shape
    img = img[h//2:3*h//4,w//2:3*w//4]
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    st.image(img)