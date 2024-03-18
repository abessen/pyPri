from PIL import Image
import streamlit as st
import os
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

st.markdown("""
    <style>
    .reportview-container .viewer .stApp .footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    body {
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize or load the session state for tracking last update time
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()

# Load the image once and store it globally
image_path = "ColLSToday1.jpg"
image = Image.open(image_path)

def main():
    # Display the image to automatically resize with the column width
    st.image(image, use_column_width=True)
    
    # Check if 60 seconds have passed
    current_time = time.time()
    if current_time - st.session_state.last_update > 60:
        st.session_state.last_update = current_time
        st.experimental_rerun()

if __name__ == '__main__':
    main()
