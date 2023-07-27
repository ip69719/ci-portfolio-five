import streamlit as st


def page_cherry_leaf_visualiser_body():
    st.write("### Cherry Leaf Visualiser")
    st.info(
        f"The Client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf "
        f"from one with powdery mildew.\n"

    )

    version = 'v1'

    if st.checkbox("Difference between average and variability images"):
        st.warning("Average and variability of images per label goes here")

    if st.checkbox("Difference between average healthy leaf and average leaf with powdery mildew"):
        st.warning("Difference between average healthy leaf and average leaf with powdery mildewgoes here")

    if st.checkbox("Image montage"):
        st.warning("Image montage goes here")
