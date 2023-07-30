import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_cherry_leaf_visualiser import page_cherry_leaf_visualiser_body
from app_pages.page_mildew_detection import page_mildew_detection_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_body

# create an instance of MultiPage class
app = MultiPage(app_name = "Cherry Leaf Powdery Mildew Detector")

# add app pages here using .add_page() method
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cherry Leaf Visualiser", page_cherry_leaf_visualiser_body)
app.add_page("Mildew Detector", page_mildew_detection_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_body)

app.run()
