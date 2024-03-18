from PIL import Image
import streamlit as st
import threading
import time  # Import the time module

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

def your_function_to_update():
    # Refresh the image
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

def rerun_thread():
    # Sleep for 60 seconds
    time.sleep(60)
    # Rerun the streamlit app
    threading.Thread(target=your_function_to_update).start()

def main():
    # Display the image to automatically resize with the column width
    st.image(image, use_column_width=True)

    # Start a thread to rerun the app after 60 seconds
    threading.Thread(target=rerun_thread, daemon=True).start()

    

if __name__ == '__main__':
    main()
