import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects a wide range of plants."
        f"* It is one of the easier plant diseases to identify, as its symptoms are quite distinctive.\n"
        f"* Infected plants display white powdery spots on the leaves.\n"
        f"* Visual criteria are used to verify if the tree leaf is healthy or has powdery mildew..\n"

        
        f"* The Client is facing a challenge where their cherry plantations have been presenting powdery mildew."
        f"The cherry plantation crop is one of the finest products in the portfolio and "
        f"the company is concerned about supplying the market with a product of compromised quality.\n\n"

        f"**Project Dataset**\n"
        f"* The available dataset contains over four thousand images taken from the Client's crop fields."
        f"* The images show healthy cherry leaves and cherry leaves that have powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ip69719/ci-portfolio-five/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf "
        f"from one with powdery mildew."
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )
