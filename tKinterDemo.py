import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the Tkinter window
root = tk.Tk()
root.title("Display Image")

# Set background color to black
root.configure(background='black')

# Load the image
image_path = r"C:\pyPri\ColLSToday2.jpg"
image = Image.open(image_path)

# Adjust window size based on image dimensions
window_width = min(root.winfo_screenwidth(), image.width + 20)
window_height = min(root.winfo_screenheight(), image.height + 20)
root.geometry(f"{window_width}x{window_height}")

# Convert Image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=tk_image)
label.place(x=10, y=10)  # Adjust position as needed

# Run the Tkinter event loop
root.mainloop()
