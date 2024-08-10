# 🎧 CompressBot 🎥

Welcome to **CompressBot**—your all-in-one Telegram bot for compressing audio and video files with ease! 🚀

## 🌟 Features

- **Compress Audio 🎧**: Convert and compress your audio files to a smaller size while maintaining good quality.
- **Compress Video 🎥**: Reduce the size of your video files with efficient compression without significant loss in quality.
- **User-Friendly**: Simple commands and easy-to-use interface.
- **Fast Processing ⚡**: Get your compressed files quickly.

## 🛠 Installation

Follow these steps to set up the bot locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/superhexa/CompressBot.git
   cd CompressBot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Open the `config.py` file in the root directory.
   - Add your credentials:
     ```python
     API_ID = 'api_id'
     API_HASH = 'api_hash'
     API_TOKEN = 'bot_token'
     ```

4. **Run the bot**:
   ```bash
   python bot.py
   ```

## 📦 Requirements

- Python 3.7+
- [Pyrogram](https://docs.pyrogram.org/) - For Telegram bot API interaction
- [Pydub](https://pydub.com/) - For audio processing
- [FFmpeg](https://ffmpeg.org/) - For video compression

## 🚀 Usage

1. **Start the bot** by sending the `/start` command.
2. **Choose** between compressing audio or video files.
3. **Upload** your media file.
4. **Receive** the compressed file instantly!

## 🛠 Configuration

You can adjust the compression parameters in the script to suit your needs:

- **Audio Compression**: Adjust the `bitrate` and `format` in the `handle_audio` function.
- **Video Compression**: Modify the FFmpeg command in the `handle_video` function to tweak video resolution, bitrate, etc.

## 🐛 Issues

If you encounter any issues or have suggestions, please feel free to open an [issue](https://github.com/superhexa/CompressBot/issues) or submit a pull request.

## 📜 License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

**Enjoy CompressBot and make your media sharing easier! 🎉**
