# Splif 1.0.0
# Coded by Judith Greaney 2023
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def frame_extract(gif_path, dest, quality):  # Frame extraction function
    img = Image.open(gif_path)
    gif_name = os.path.splitext(os.path.basename(gif_path))[0]
    os.makedirs(os.path.join(dest, gif_name), exist_ok=True)
    try:
        frame = 0
        while True:
            current_frame = img.copy()
            current_frame = current_frame.convert('RGB')
            current_frame.save(f"{dest}/{gif_name}/frame{img.tell()}.{selected_option.get()}", quality=quality)
            frame += 1
            img.seek(frame)
    except EOFError:
        pass
    finally:
        img.close()

def browse_gif():
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    gif_path_entry.delete(0, tk.END)
    gif_path_entry.insert(0, file_path)

def browse_dest():
    dest_folder = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_folder)

def split_gif():
    gif_path = gif_path_entry.get()
    dest = dest_entry.get()
    quality = quality_slider.get()
    try:
        frame_extract(gif_path, dest, quality)
        status_label.config(text="GIF Splitting Complete!")
    except FileNotFoundError:
        status_error.config(text="File/Folder doesn't exist or can't be accessed.")
    root.after(5000, clear_status_messages)

def show_about():
    tk.messagebox.showinfo(title="About", message="Placeholder")

def clear_status_messages():
    status_label.config(text="")
    status_error.config(text="")

# Tkinter config
root = tk.Tk()  # Creates the main window
root.title("Splif GUI v1.0.0")  # Titles the window
root.resizable(False, False)  # Makes the window a fixed size

# Creates and configures frames
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Creates a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="About", command=show_about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# Creates and configures labels and buttons for GIF input/output
gif_path_label = tk.Label(frame, text="Select a GIF:")
gif_path_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
gif_path_entry = tk.Entry(frame, width=40)
gif_path_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)
browse_gif_button = tk.Button(frame, text="Browse", command=browse_gif)
browse_gif_button.grid(row=0, column=3, padx=10, pady=5)
dest_label = tk.Label(frame, text="Select Output Folder:")
dest_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
dest_entry = tk.Entry(frame, width=40)
dest_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
browse_dest_button = tk.Button(frame, text="Browse", command=browse_dest)
browse_dest_button.grid(row=1, column=3, padx=10, pady=5)

# dropdown for output format
option_label = tk.Label(frame, text="Select a format:")
option_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
options = ["JPG", "PNG", "BMP"]  # output format options
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Sets the default selected option
dropdown_menu = tk.OptionMenu(frame, selected_option, *options)
dropdown_menu.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Quality slider
quality_label = tk.Label(frame, text="Select Quality(1-100):")
quality_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
quality_slider = tk.Scale(frame, from_=1, to=100, orient="horizontal")
quality_slider.set(80)  # Sets the default quality
quality_slider.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Split button
split_button = tk.Button(frame, text="Split GIF", command=split_gif)
split_button.grid(row=4, columnspan=4, padx=10, pady=10)

# Status label/error
status_label = tk.Label(frame, text="", fg="green", width=40)
status_label.grid(row=5, column=0, columnspan=4)
status_error = tk.Label(frame, text="", fg="red")
status_error.grid(row=6, column=0, columnspan=4)

# Start the Tkinter main loop
root.mainloop()
