import streamlit as st
import os
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_cherry_leaf_visualiser_body():
    st.write("### Cherry Leaf Visualiser")
    st.info(
        f"The Client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf "
        f"from one with powdery mildew.\n"

    )

    version = 'v1'

    if st.checkbox("Difference between average and variability images"):
        st.warning(
            f"* We notice the average and variability images did not show "
            f"patterns where we could intuitively differentiate one from "
            f"another. However, a small difference in the colour pigment of "
            f"the average images is seen for both labels.")

        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(
            avg_powdery_mildew,
            caption='Leaf with powdery mildew - Average and Variability'
            )
        st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Difference between average healthy leaf and average leaf with powdery mildew"):  # noqa:E501

        st.warning(
            f"* We notice this study did not show patterns where we could "
            f"intuitively differentiate one from another.")

        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(
            diff_between_avgs, caption='Difference between average images')
        st.write("---")

    if st.checkbox("Image montage"):
        my_data_dir = 'inputs/mildew_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(
                dir_path=my_data_dir + '/validation',
                label_to_display=label_to_display,
                nrows=3, ncols=3, figsize=(10, 12)
                )


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(10, 12)):
    """
    copy function from 02 - DataVisualization.ipynb notebook
    called when Create Montage button is clicked

    The function
    * checks if the label exists in the directory
    * checks if montage space is greater than the subset size
    * creates a list of axes indices based on nb of rows and number of columns
    * creates a figure and display images
    * loads and plots the images using a loop
    """

    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:
        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
