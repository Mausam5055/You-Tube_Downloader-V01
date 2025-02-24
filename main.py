import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import threading
import os
try:
    from utils import download_video, convert_to_mp3
except ImportError:
    messagebox.showerror("Error", "utils.py not found! Ensure it exists in the same directory.")
    exit()

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Initialize UI elements
        self.create_widgets()

    def create_widgets(self):
        """Creates UI components."""
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=15)

        # Logo
        try:
            img = Image.open("assets/icon.ico")
            img = img.resize((50, 50), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(img)
            ttk.Label(header_frame, image=self.logo).pack(side=tk.LEFT)
        except FileNotFoundError:
            self.logo = None

        # Title
        ttk.Label(header_frame, text="YouTube Downloader",
                  font=("Helvetica", 16, "bold")).pack(side=tk.LEFT, padx=10)

        # Main content
        main_frame = ttk.Frame(self.root)
        main_frame.pack(pady=15, padx=40, fill=tk.BOTH)

        # URL Entry
        ttk.Label(main_frame, text="YouTube URL:").grid(row=0, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=0, column=1, pady=5)

        # Download Path
        ttk.Label(main_frame, text="Download Path:").grid(row=1, column=0, sticky=tk.W)
        self.path_entry = ttk.Entry(main_frame, width=50)
        self.path_entry.grid(row=1, column=1, pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_directory).grid(row=1, column=2, padx=5)

        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=3, pady=20)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Download Video", command=self.start_video_download).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Convert to MP3", command=self.start_mp3_conversion).pack(side=tk.LEFT, padx=10)

        # Status Label
        self.status_label = ttk.Label(main_frame, text="", font=("Helvetica", 10, "italic"))
        self.status_label.grid(row=4, column=0, columnspan=3)

    def browse_directory(self):
        """Opens a file dialog to select download directory."""
        directory = filedialog.askdirectory()
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)

    def start_video_download(self):
        """Starts video download in a separate thread."""
        url, path = self.get_inputs()
        if not url or not path:
            return
        threading.Thread(target=self.download_video, args=(url, path), daemon=True).start()

    def start_mp3_conversion(self):
        """Starts MP3 conversion in a separate thread."""
        url, path = self.get_inputs()
        if not url or not path:
            return
        threading.Thread(target=self.convert_to_mp3, args=(url, path), daemon=True).start()

    def get_inputs(self):
        """Validates and returns URL & path."""
        url = self.url_entry.get().strip()
        path = self.path_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return None, None
        if not path:
            messagebox.showerror("Error", "Please select a download path.")
            return None, None
        if not os.path.exists(path):
            messagebox.showerror("Error", "Invalid path. Please select an existing folder.")
            return None, None
        return url, path

    def download_video(self, url, path):
        """Handles video download."""
        self.update_ui("Downloading video...")
        try:
            download_video(url, path, self.update_progress)
            self.show_message("Success", "Video downloaded successfully!")
        except Exception as e:
            self.show_message("Error", str(e))
        finally:
            self.reset_ui()

    def convert_to_mp3(self, url, path):
        """Handles MP3 conversion."""
        self.update_ui("Converting to MP3...")
        try:
            convert_to_mp3(url, path, self.update_progress)
            self.show_message("Success", "MP3 converted successfully!")
        except Exception as e:
            self.show_message("Error", str(e))
        finally:
            self.reset_ui()

    def update_progress(self, d):
        """Handles progress update from yt-dlp."""
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 1)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            percentage = (downloaded_bytes / total_bytes) * 100

            # Use `config(value=...)` instead of `.set()`
            self.root.after(100, lambda: self.progress.config(value=percentage))

    def reset_ui(self):
        """Resets UI elements after download."""
        self.root.after(100, lambda: self.progress.config(value=0))
        self.root.after(100, lambda: self.status_label.config(text=""))
        self.root.after(100, lambda: self.url_entry.delete(0, tk.END))

    def update_ui(self, text):
        """Updates status label text."""
        self.root.after(100, lambda: self.status_label.config(text=text))

    def show_message(self, title, message):
        """Displays a messagebox."""
        self.root.after(100, lambda: messagebox.showinfo(title, message))

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
