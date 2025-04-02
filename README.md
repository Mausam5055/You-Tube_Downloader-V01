# YouTube Video & MP3 Downloader 🎥🎵

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pytube](https://img.shields.io/badge/Library-Pytube-orange)](https://pytube.io/)

A modern Python-based tool for downloading YouTube videos and converting them to MP3 format. Simple, efficient, and user-friendly.

## ✨ Features

- 🎥 Download YouTube videos in MP4 format
- 🎵 Convert YouTube videos to MP3 format
- 📂 Customizable download directory
- ⚡ Fast and efficient downloads
- 🔒 No web server required
- 🎨 Clean command-line interface

## 🖼️ Preview

![Preview Image](preview.png)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mausam5055/You-Tube_Downloader-V01.git
   cd You-Tube_Downloader-V01
   ```

2. **Install dependencies**
   ```bash
   pip install pytube
   ```

3. **Run the script**
   ```bash
   python downloader.py
   ```

## 📋 Prerequisites

- Python 3.7 or higher
- FFmpeg (for MP3 conversion)

### Installing FFmpeg

#### Windows
1. Download from [FFmpeg Official Builds](https://ffmpeg.org/download.html)
2. Extract the ZIP file
3. Add `ffmpeg/bin` to your system PATH
4. Verify installation:
   ```bash
   ffmpeg -version
   ```

#### macOS
```bash
brew install ffmpeg
```

#### Linux
```bash
sudo apt update && sudo apt install ffmpeg
```

## 💡 Usage

### Basic Usage
```bash
python downloader.py
```

### Direct URL Download
```bash
python downloader.py "https://www.youtube.com/watch?v=your_video_id"
```

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `pytube` not found | Run `pip install pytube` |
| FFmpeg errors | Verify PATH configuration |
| Download failures | Check URL validity |
| MP3 conversion issues | Ensure FFmpeg is properly installed |

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mausam Kar**
- [GitHub](https://github.com/Mausam5055/)
- [Contributions Welcome](https://github.com/Mausam5055/You-Tube_Downloader-V01/issues)

---
Made with ❤️ by Mausam Kar

