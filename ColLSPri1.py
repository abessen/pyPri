from PIL import Image
import streamlit as st
import subprocess
import time
import os
import win32com.client

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

# Function to rerun the Streamlit app/script using Streamlit's experimental rerun feature
def rerun():
    st.experimental_rerun()
    

# Cache the function that loads the image
#@st.cache_data
def load_image(image_path):
    return Image.open(image_path)


def main():
    # Add buttons for running the external programs in the sidebar
    if st.sidebar.button('ReFresh Data'):
        try:
            subprocess.call([r"C:\pyRun1\pushOlenPrimary.bat"])
        except Exception as e:
            print("Error executing pushOlenPrimary.bat:", e)

    if st.sidebar.button('Set Schedule'):
        try:
            process = subprocess.Popen(["streamlit", "run", r"C:\pyRun1\SetSchedule.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stdout:
                print("SetSchedule.py stdout:", stdout.decode())
            if stderr:
                print("SetSchedule.py stderr:", stderr.decode())
        except Exception as e:
            print("Error executing SetSchedule.py:", e)

    # Add code to run the batch files silently
    wsh = win32com.client.Dispatch("WScript.Shell")
    path1 = "C:\\pyDash1\\pushOlenPrimary.bat"  # Update this to the path of your first batch file
    os.chdir("C:\\pyDash1")
    cmd1 = "cmd /c " + '"' + path1 + '"'  # Run the first batch file invisibly
    wsh.Run(cmd1, 0, True)

    path2 = "C:\\pyPri\\pushOlenPrimary.bat"  # Update this to the path of your second batch file
    os.chdir("C:\\pyPri")
    cmd2 = "cmd /c " + '"' + path2 + '"'  # Run the second batch file invisibly
    wsh.Run(cmd2, 0, True)

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
    image_path = "ColLSToday1.jpg"

    # Load the image using the cached function
    image = load_image(image_path)

    # Display the image to automatically resize with the column width
    st.image(image, use_column_width=True)

    # Wait for 60 seconds before the next iteration
    time.sleep(30)  
    rerun()


if __name__ == '__main__':
    main()
