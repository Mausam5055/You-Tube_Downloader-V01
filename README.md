# YouTube Video & MP3 Downloader (Version 1) 🎥🎵

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pytube](https://img.shields.io/badge/Library-Pytube-orange)](https://pytube.io/)

A simple **Python script** to download YouTube videos as MP4 or convert them to MP3 **without using a web server**.

## Table of Contents
- [Features](#-features)
- [Preview](#-preview)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Author](#-author)
- [What's Next?](#-whats-next)

---

## 🚀 Features
- 👥 Download YouTube videos in MP4 format
- 🎷 Convert YouTube videos to MP3 format
- 📂 Saves files in a user-specified directory
- 🔥 No extra setup required, runs with a simple command

---

## 📌 Preview
![Preview Image](preview.png)  


---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- `pytube` library for downloading YouTube videos
- `ffmpeg` (optional, for MP3 conversion)

### Install Dependencies
```sh
pip install pytube
```
For MP3 conversion, install FFmpeg:

#### Windows
- Download from [FFmpeg Official Builds](https://ffmpeg.org/download.html)
- Extract ZIP and add `ffmpeg/bin` to system `PATH`
- Verify installation:
  ```sh
  ffmpeg -version
  ```

#### macOS (Homebrew)
```sh
brew install ffmpeg
```

#### Linux (Debian/Ubuntu)
```sh
sudo apt update && sudo apt install ffmpeg
```

---

## ▶️ Usage
Run the script:
```sh
python downloader.py
```
OR
Run with a specific YouTube URL:
```sh
python downloader.py "https://www.youtube.com/watch?v=your_video_id"
```

---

## 🌟 downloader.py (Main Script)
```python
import os
import sys
import pytube

# Function to download video
def download_video(url, output_path):
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        print(f"Downloading: {yt.title}")
        stream.download(output_path)
        print(f"Downloaded Successfully: {yt.title}\nSaved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Function to convert to MP3
def convert_to_mp3(video_path):
    try:
        mp3_path = video_path.replace(".mp4", ".mp3")
        os.system(f'ffmpeg -i "{video_path}" -q:a 0 -map a "{mp3_path}" -y')
        print(f"Converted to MP3: {mp3_path}")
    except Exception as e:
        print(f"MP3 Conversion Failed: {e}")

# Main function
def main():
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter YouTube Video URL: ")

    output_directory = "Downloads"
    os.makedirs(output_directory, exist_ok=True)

    download_video(video_url, output_directory)

    choice = input("Convert to MP3? (y/n): ").strip().lower()
    if choice == "y":
        video_file = os.path.join(output_directory, pytube.YouTube(video_url).streams.first().default_filename)
        convert_to_mp3(video_file)

if __name__ == "__main__":
    main()
```

---

## 🔧 Troubleshooting
| Issue | Solution |
|--------|----------|
| `pytube` not found | Install with `pip install pytube` |
| `FFmpeg` not found | Verify `PATH` configuration, restart terminal |
| Download fails | Check YouTube URL validity |
| MP3 conversion fails | Ensure `FFmpeg` is installed and configured properly |

---

## 🌜 License
Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

## 👨‍💻 Author
**Mausam Kar**  
[GitHub](https://github.com/Mausam5055/)  
Contributions & suggestions welcome! 🚀

