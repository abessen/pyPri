import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the Tkinter window
root = tk.Tk()
root.title("Display Image")

# Set background color to black
root.configure(background='black')

# Define the default value for the first combobox
default_value1 = tk.StringVar(value="12:01 AM")

# Define the default value for the second combobox
default_value2 = tk.StringVar(value="12:01 AM")

# Define custom style for the first dropdown
style1 = ttk.Style()
style1.theme_use('clam')  # Use the 'clam' theme for the style
style1.configure('Custom.TCombobox1', fieldbackground='gray')  # Set background color to gray

# Define custom style for the second dropdown
style2 = ttk.Style()
style2.theme_use('clam')  # Use the 'clam' theme for the style
style2.configure('Custom.TCombobox2', fieldbackground='gray')  # Set background color to gray

HrSel = ("12:01 AM", "12:30 AM", "1:00 AM", "1:30 AM", "2:00 AM", "2:30 AM", "3:00 AM", "3:30 AM", "4:00 AM",
         "4:30 AM", "5:00 AM", "5:30 AM", "6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", "9:00 AM",
         "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM",
         "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM",
         "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM",
         "11:30 PM")

# Load the image
image_path = r"C:\pyPri\ColLSToday2.jpg"
image = Image.open(image_path)

# Adjust window size based on image dimensions
window_width = min(root.winfo_screenwidth(), image.width)
window_height = min(root.winfo_screenheight(), image.height)
root.geometry(f"{window_width}x{window_height}")

# Convert Image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=tk_image)
label.place(x=0, y=0)  # Place the image at the top-left corner of the window

# Create Dropdownbox1
start_combo1 = ttk.Combobox(root, values=HrSel, width=9, height=1, font=('Helvetica', 11), textvariable=default_value1, style='Custom.TCombobox1')  
start_combo1.place(x=100, y=10)  # Adjust the coordinates for indentation

# Create Dropdownbox2
start_combo2 = ttk.Combobox(root, values=HrSel, width=9, height=1, font=('Helvetica', 11), textvariable=default_value2, style='Custom.TCombobox2')  
start_combo2.place(x=100, y=40)  # Adjust the coordinates for indentation

# Run the Tkinter event loop
root.mainloop()
