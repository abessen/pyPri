from PIL import Image
import streamlit as st
import threading
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

# Function to update the displayed image
def update_image(image_container):
    new_image = Image.open(image_path)
    image_container.image(new_image, use_column_width=True)

def update_loop(image_container):
    while True:
        # Update the image every 60 seconds
        time.sleep(60)
        # Call the update_image function to refresh the image
        update_image(image_container)

def main():
    # Display the image initially
    image_container = st.empty()
    update_image(image_container)

    # Start a separate thread to handle the update loop
    update_thread = threading.Thread(target=update_loop, args=(image_container,))
    update_thread.start()

if __name__ == '__main__':
    main()
