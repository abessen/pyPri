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

def your_function_to_update(image_container):
    # Refresh the image
    new_image = Image.open(image_path)
    image_container.image(new_image, use_column_width=True)

def rerun_thread(image_container):
    while True:  # Run indefinitely
        # Sleep for 60 seconds
        time.sleep(60)
        # Rerun the update function
        your_function_to_update(image_container)

def main():
    # Display the image to automatically resize with the column width
    st.image(image_path, use_column_width=True)

    # Keep updating the image every 60 seconds
    while True:
        time.sleep(60)
        # Force Streamlit to rerun the loop by modifying a widget
        st.write(f"Updating at: {time.strftime('%H:%M:%S')}")

if __name__ == '__main__':
    main()

