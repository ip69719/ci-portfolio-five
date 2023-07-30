import streamlit as st


def project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect cherry leaves infected with powdery mildew to have "
        f"white powdery looking patches differentiating them from healthy "
        f"green leaves. \n\n"
        f"* An Image Montage shows that leaves containing powdery mildew "
        f"typically have white patches on them. Healthy leaves are light "
        f"to dark green in colour. Average Image, Variability Image and "
        f"Difference between Averages studies did not reveal any clear "
        f"pattern to differentiate one from another."
    )
