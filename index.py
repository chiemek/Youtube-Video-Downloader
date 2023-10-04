import tkinter as tk
from tkinter import messagebox
import pytube
import os

# Function to download the YouTube video
def download_video():
    video_url = url_entry.get()
    try:
        video_instance = pytube.YouTube(video_url)
        stream = video_instance.streams.get_highest_resolution()
        download_location = os.path.expanduser("~\Downloads")
        stream.download(output_path=download_location)
        messagebox.showinfo("Success", "Video downloaded successfully to your 'Downloads' directory!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("YouTube Video Downloader")


# Create and place widgets
label = tk.Label(app, text="Enter YouTube URL:")
label.pack()

url_entry = tk.Entry(app, width=50)
url_entry.pack()

download_button = tk.Button(app, text="Download Video", command=download_video)
download_button.pack()

# Run the application
app.mainloop()