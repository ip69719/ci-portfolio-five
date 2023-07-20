import streamlit as st

class MultiPage:
# Class to generate multiple Streamlit pages using an object oriented approach
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        # configure the page using streamlit method
        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")

    # method to add pages
    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        # create title on each page
        st.title(self.app_name)
        # sidebar menu consisting of radio buttons
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
