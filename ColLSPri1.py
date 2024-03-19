from PIL import Image
import streamlit as st
import time


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
image_path = "ColLSPri.jpg"
image = Image.open(image_path)

def main():
    # Display the image initially
    image_container = st.empty()
    image_container.image(image, use_column_width=True)

    # Keep updating the image every 60 seconds
    while True:
     #   time.sleep(60)
        
        # Update the image in-place
        updated_image = Image.open(image_path)
      #  image_container.image(updated_image, use_column_width=True)

if __name__ == '__main__':
    main()
