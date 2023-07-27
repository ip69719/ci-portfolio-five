import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread


def page_cherry_leaf_visualiser_body():
    st.write("### Cherry Leaf Visualiser")
    st.info(
        f"The Client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf "
        f"from one with powdery mildew.\n"

    )

    version = 'v1'

    if st.checkbox("Difference between average and variability images"):
        avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(avg_powdery_mildew, caption='Leaf with powdery mildew - Average and Variability')
        st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Difference between average healthy leaf and average leaf with powdery mildew"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(diff_between_avgs, caption='Difference between average images')
        st.write("---")

    if st.checkbox("Image montage"):
        st.warning("Image montage goes here")
