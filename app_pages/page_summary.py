import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"

        f"* The Client is facing a challenge where their cherry plantations "
        f"have been presenting powdery mildew. The cherry plantation crop is "
        f"one of the finest products in the portfolio and the company "
        f"concerned about supplying the market with a product of compromised "
        f"quality.\n"
        f"* Powdery mildew is a fungal disease that affects a wide range of "
        f"plants.\n"
        f"* It is one of the easier plant diseases to identify, as its "
        f"symptoms are quite distinctive.\n"
        f"* Infected plants display white powdery spots on the leaves.\n"
        f"* Visual criteria are used to verify if the tree leaf is healthy or "
        f"has powdery mildew.\n\n"

        f"**Project Dataset**\n"
        f"* The available dataset contains over four thousand images taken "
        f"from the Client's crop fields.\n"
        f"* The images show healthy cherry leaves and cherry leaves that "
        f"have powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ip69719/ci-portfolio-five/blob/main/README.md).")  # noqa:E501

    st.success(
        f"**Business Requirements**\n\n"
        f"The project has two business requirements:\n"
        f"* 1 - The Client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf "
        f"from one with powdery mildew.\n"
        f"* 2 - The Client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew. "
        )
