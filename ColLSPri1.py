from PIL import Image
import streamlit as st

# Set Page Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  

st.markdown(
    """
    <style>
    .reportview-container .viewer .stApp .footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the image once and store it globally
@st.experimental_singleton
def load_image(image_path):
    return Image.open(image_path)

def main():
    # Display the image to automatically resize with the column width
    image_path = "ColLSPri.jpg"
    image = load_image(image_path)
    st.image(image, use_column_width=True)

if __name__ == '__main__':
    main()
