import tkinter as tk
from tkinter import filedialog
from PIL import Image

def frameExtract(gifpath, dest):
    img = Image.open(gifpath)
    try:
        frame = 0
        while True:
            currentframe = img.copy()
            currentframe = currentframe.convert('RGB')
            currentframe.save(f"{dest}/frame{img.tell()}.jpg")
            frame += 1
            img.seek(frame)
    except EOFError:
        pass
    finally:
        img.close()

def browse_gif():
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    gifpath_entry.delete(0, tk.END)
    gifpath_entry.insert(0, file_path)

def browse_dest():
    dest_folder = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_folder)

def split_gif():
    gifpath = gifpath_entry.get()
    dest = dest_entry.get()
    try:
        frameExtract(gifpath, dest)
        status_label.config(text="GIF Splitting Complete!")
    except FileNotFoundError:
        status_error.config(text="File/Folder doesn't exist or can't be accessed.")
    root.after(5000, clear_status_messages)  # Schedule the function to clear messages after 5 seconds

def clear_status_messages():
    status_label.config(text="")
    status_error.config(text="")

# Create the main window
root = tk.Tk()
root.title("Splif GUI v0.1.0")
root.resizable(False, False)

# Create and configure frames
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Create and configure labels and buttons
gifpath_label = tk.Label(frame, text="Select a GIF:")
gifpath_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

gifpath_entry = tk.Entry(frame, width=40)
gifpath_entry.grid(row=0, column=1, padx=10, pady=5)

browse_gif_button = tk.Button(frame, text="Browse", command=browse_gif)
browse_gif_button.grid(row=0, column=2, padx=10, pady=5)

dest_label = tk.Label(frame, text="Select Output Folder:")
dest_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

dest_entry = tk.Entry(frame, width=40)
dest_entry.grid(row=1, column=1, padx=10, pady=5)

browse_dest_button = tk.Button(frame, text="Browse", command=browse_dest)
browse_dest_button.grid(row=1, column=2, padx=10, pady=5)

split_button = tk.Button(frame, text="Split GIF", command=split_gif)
split_button.grid(row=2, columnspan=3, padx=10, pady=10)

status_label = tk.Label(frame, text="", fg="green", width=40)  # Adjust width as needed
status_label.grid(row=3, column=0, columnspan=3)  # Use a separate row for status_label

status_error = tk.Label(frame, text="", fg="red")
status_error.grid(row=4, column=0, columnspan=3)  # Use a separate row for status_error

# Start the Tkinter main loop
root.mainloop()
