import tkinter as tk
from PIL import ImageTk, Image
import streamlit as st
import subprocess
import time
import cv2
import numpy as np

# Set Page Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Inject custom CSS for title styling
st.markdown("""
        <style>
        .title-font {
            font-family: 'Arial Nova', Arial, sans-serif;
            font-size: 14px !important;
        }
        </style>
    """, unsafe_allow_html=True)

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

# Function to capture image using tkinter
def capture_image():
    # Create a tkinter window
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()  # Hide the main window

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Capture the image
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Close the tkinter window
    root.destroy()

    # Convert the image from OpenCV format to PIL format
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    return image

def main():
    if 'last_run' not in st.session_state:
        st.session_state.last_run = time.time()

    while True:
        # Run the shell script to refresh data
        try:
            subprocess.call(["C:/pyPri/pushOlenPrimary.bat"])  # Update with the correct path
        except Exception as e:
            print("Error executing pushOlenPrimary.bat:", e)

        # Inject custom CSS for sidebar background color
        st.markdown(
            """
            <style>
            .sidebar .sidebar-content {
                background-color: #000080; /* Dark blue sidebar background */
                color: white; /* Text color */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Capture the image
        image = capture_image()

        # Display the captured image
        st.image(image, use_column_width=True)

        # Wait for 30 seconds before the next iteration
        time.sleep(30)  

        # Rerun the Streamlit app
        st.experimental_rerun()

if __name__ == '__main__':
    main()
