import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def update_date():
    current_date = datetime.now().strftime("%A, %d %B %Y")
    date_label.config(text=current_date)
    date_label.after(60000, update_date)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("500x350")
window.resizable(False, False)

# Configure the background color
window.configure(bg="#FFFFFF")  # Set the background color to white

# Create the modern border with background shadow
border_frame = tk.Frame(window, bg="#FF9F00", bd=0, highlightbackground="#FF9F00", highlightcolor="#FF9F00", highlightthickness=10)
border_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER, width=460, height=220)  # Adjust the height to accommodate the labels

# Create the clock label
time_label = tk.Label(border_frame, font=("Century Gothic", 80), fg="white", bg="#FF9F00")
time_label.pack(pady=30)  # Add vertical padding to the clock label
update_time()

# Create the date label
date_label = tk.Label(border_frame, font=("Century Gothic", 16), fg="white", bg="#FF9F00", anchor="center")
date_label.pack(pady=(10, 20))  # Add vertical padding to the date label
update_date()

# Create a frame for the footer
footer_frame = tk.Frame(window, bg="#FF7F00", bd=1, relief="sunken")  # Add a border and change the bg color to darker orange
footer_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor='s')

# Create a label for the developer info inside the footer frame
dev_info = tk.Label(footer_frame, text="Developed by: Abhishek Shah | Developed Year: 2020", bg="#FF7F00", fg="#FFFFFF")  # Change text color to white for better contrast
dev_info.pack(anchor='center')

window.mainloop()
