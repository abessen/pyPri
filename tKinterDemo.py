import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from openpyxl import Workbook

def update_label1(event):
    value = start_combo1.get()
    label1.config(text=value)
    save_to_excel(value)

def save_to_excel(value):
    wb = Workbook()
    ws = wb.active    
    ws.append([value])
    wb.save("start.xlsx")

# Create the Tkinter window
root = tk.Tk()
root.title("Display Image")

# Set background color to black
root.configure(background='black')

# Define custom style for the dropdown
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for the style
style.configure('Custom.TCombobox', fieldbackground='black')  # Set background color to gray

HrSel = ("12:01 AM", "12:30 AM", "1:00 AM", "1:30 AM", "2:00 AM", "2:30 AM", "3:00 AM", "3:30 AM", "4:00 AM",
         "4:30 AM", "5:00 AM", "5:30 AM", "6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", "9:00 AM",
         "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM",
         "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM",
         "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM", "9:30 PM", "10:00 PM", "10:30 PM", "11:00 PM",
         "11:30 PM")

RateSel = ("200", "250", "300", "350", "400", "450", "500", "550", "600", "650", "700", "750", "800", "850", "900",
           "950", "1000", "1050", "1100", "1150", "1200", "1250", "1300", "1350", "1400", "1450", "1500", "1550",
           "1600", "1650", "1700", "1750", "1800", "1850", "1900", "1950", "2000", "2050", "2100", "2150", "2200",
           "2250", "2300", "2400")

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

# Create the first Dropdownbox
start_combo1 = ttk.Combobox(root, values=HrSel, width=9, height=1, font=('Helvetica', 11), style='Custom.TCombobox')  # Adjust font size as needed
start_combo1.place(x=134, y=14)  # Adjust the coordinates for indentation
start_combo1.bind("<<ComboboxSelected>>", update_label1)

# Create labels to display the selections
label1 = tk.Label(root, text="", font=('Helvetica', 11), bg="black", fg="white")
label1.place(x=start_combo1.winfo_x() + 5, y=start_combo1.winfo_y() + start_combo1.winfo_height() + 1)

# Run the Tkinter event loop
root.mainloop()
