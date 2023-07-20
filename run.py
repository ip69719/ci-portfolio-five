import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body

# create an instance of MultiPage class
app = MultiPage(app_name = "Cherry Leaf Powdery Mildew Detector")

# add app pages here using .add_page() method
app.add_page("Quick Project Summary", page_summary_body)

app.run()
