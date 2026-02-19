# YouTube Downloader 🎥🎶

A simple yet powerful **YouTube Downloader GUI application** built with **Python 3.14**, **Tkinter**, and **Pytube**.  
It allows users to download YouTube videos in **MP4 format** or extract audio in **MP3 format** using **FFmpeg**.

---

## ✨ Features
- 📺 Download YouTube videos in **MP4** (video + audio combined).
- 🎵 Extract and save audio in **MP3** format.
- 📂 Choose custom download folder.
- 📊 Real-time progress updates during download.
- 🖥️ User-friendly **Tkinter GUI** interface.
- ⚡ Multithreaded downloads (no UI freezing).
- 🛠️ Error handling with clear messages.

---

## 🛠️ Requirements
Make sure you have the following installed:

- **Python 3.14+**
- **pip** (Python package manager)
- **FFmpeg** (for audio conversion)

### Install dependencies:
```bash
pip install pytube
```

### Install FFmpeg:
- **Windows:** Download from FFmpeg official site (ffmpeg.org in Bing) [(bing.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.bing.com%2Fsearch%3Fq%3D%2522https%253A%252F%252Fffmpeg.org%252Fdownload.html%2522") and add to PATH.
- **Linux/macOS:**  
  ```bash
  sudo apt install ffmpeg   # Ubuntu/Debian
  brew install ffmpeg       # macOS (Homebrew)
  ```

---

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/SUBHADEEPBAG300/youtube-downloader.git
   cd youtube-downloader
   ```

2. Run the application:
   ```bash
   python youtube_downloader.py
   ```

3. Steps inside the app:
   - Enter a YouTube video URL.
   - Select a download folder.
   - Click **Download Video (MP4)** or **Download Audio (MP3)**.
   - Monitor progress in the GUI.
   - Success message will show the file location.

---

## ⚠️ Notes
- Ensure your internet connection is stable during downloads.
- Some videos may have restrictions (age, region, DRM) and may not be downloadable.
- Audio conversion requires **FFmpeg** installed and accessible via system PATH.

---

## 📄 License
This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repo
- Create a new branch (`feature-xyz`)
- Commit changes
- Submit a Pull Request

---

## 👨‍💻 Author
Developed by **Subhadeep Bag**  
🔗 GitHub: [SUBHADEEPBAG300](https://github.com/SUBHADEEPBAG300)
