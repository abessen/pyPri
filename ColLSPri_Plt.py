from PIL import Image
import streamlit as st
import subprocess
import time

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

# Cache the function that loads the image
#@st.cache_data
def load_image(image_path):
    return Image.open(image_path)

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

        # Local path to the image
        image_path = "ColLSToday4.jpg"

        # Load the image using the cached function
        image = load_image(image_path)

        # Display the image to automatically resize with the column width
        st.image(image, use_column_width=True)

        # Wait for 30 seconds before the next iteration
        time.sleep(30)  

        # Rerun the Streamlit app
        st.experimental_rerun()

if __name__ == '__main__':
    main()
