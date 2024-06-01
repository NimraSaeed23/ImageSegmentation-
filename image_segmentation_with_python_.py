# -*- coding: utf-8 -*-
"""Image Segmentation with Python .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KuT1JKZeuT84Sqd43CAjiqBu3Ch0xoW1
"""

import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def segment_image(image, n_clusters):
    # Convert image to numpy array
    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(pixels)
    new_colors = kmeans.cluster_centers_[kmeans.labels_]
    segmented_image = new_colors.reshape(image_array.shape)
    return segmented_image

st.title('Image Segmentation App')

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Slider for choosing number of clusters
    n_clusters = st.slider('Select Number of Clusters', min_value=2, max_value=20, value=5)

    if st.button('Segment Image'):
        segmented_image = segment_image(image, n_clusters)
        st.image(segmented_image, caption='Segmented Image', use_column_width=True)





