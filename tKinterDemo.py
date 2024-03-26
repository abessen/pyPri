import tkinter as tk
from PIL import ImageTk, Image

# Create the Tkinter window
root = tk.Tk()
root.title("Display Image")

# Load the image
image_path = r"C:\pypri\pytinker\ColLSToday2.jpg"
image = Image.open(image_path)
image.thumbnail((1294, 1047))  # Resize the image as needed

# Convert Image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(root, image=tk_image)
label.pack(padx=10, pady=10)  # Add some padding

# Run the Tkinter event loop
root.mainloop()
