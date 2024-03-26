import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the Tkinter window
root = tk.Tk()
root.title("Display Image")

# Set background color to black
root.configure(background='black')

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

# Create Dropdownbox
start_combo = ttk.Combobox(root, values=HrSel, width=10, height=3, font=('Helvetica', 12))  # Adjust font size as needed
start_combo.place(x=140, y=12)  # Adjust the coordinates for indentation

# Run the Tkinter event loop
root.mainloop()
