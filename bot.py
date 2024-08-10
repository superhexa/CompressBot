import os
import tempfile
import subprocess
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pydub import AudioSegment
from config import *

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=API_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Compress Audio 🎧", callback_data="compress_audio"),
         InlineKeyboardButton("Compress Video 🎥", callback_data="compress_video")]
    ])
    message.reply_text("Choose what you want to compress:", reply_markup=markup)

@app.on_callback_query()
def callback(client, callback_query: CallbackQuery):
    callback_query.message.reply_text("Send me a file.")

@app.on_message(filters.voice | filters.audio)
def handle_audio(client, message):
    file = client.download_media(message.voice.file_id if message.chat.type == "voice" else message.audio.file_id)
    audio = AudioSegment.from_file(file)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        audio.export(temp_file.name, format="mp3", bitrate="64k")
        temp_file.seek(0)
        message.reply_document(temp_file.name)

@app.on_message(filters.video)
def handle_video(client, message):
    file = client.download_media(message.video.file_id)
    
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
        temp_filename = temp_file.name
        command = f'ffmpeg -i "{file}" -filter_complex "scale=\'min(1920,iw)\':\'min(1080,ih)\'" -r 24 -c:v libx265 -pix_fmt yuv420p -b:v 100k -crf 30 -preset fast -c:a libfdk_aac -profile:a xhe-aac -sample_fmt s16 -ar 44100 -b:a 64k -ac 1 -map_metadata -1 "{temp_filename}"'
        subprocess.run(command, shell=True, check=True)
        message.reply_video(temp_filename)
    
    os.remove(temp_filename)

app.run()
