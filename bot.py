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
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Compress Audio 🎧", callback_data="compress_audio"),
                                    InlineKeyboardButton("Compress Video 🎥", callback_data="compress_video")]])
    message.reply_text("Choose what you want to compress:", reply_markup=markup)

@app.on_callback_query()
def callback(client, callback_query: CallbackQuery):
    callback_query.message.reply_text("Send me a file.")

@app.on_message(filters.voice | filters.audio)
def handle_audio(client, message):
    file = client.download_media(message.voice.file_id if message.chat.type == "voice" else message.audio.file_id)
    audio = AudioSegment.from_file(file).set_channels(AUDIO_CHANNELS).set_frame_rate(AUDIO_SAMPLE_RATE)
    with tempfile.NamedTemporaryFile(suffix=TEMP_FILE_SUFFIX_AUDIO, delete=False) as temp_file:
        temp_filename = temp_file.name
        audio.export(temp_filename, format=AUDIO_FORMAT, bitrate=AUDIO_BITRATE)
    message.reply_document(temp_filename)
    os.remove(file)
    os.remove(temp_filename)

@app.on_message(filters.video | filters.animation)
def handle_media(client, message):
    file = client.download_media(message.video.file_id if message.video else message.animation.file_id)
    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
        temp_filename = temp_file.name
    if message.animation: subprocess.run(f'ffmpeg -i "{file}" "{temp_filename}"', shell=True, check=True)
    subprocess.run(f'ffmpeg -i "{file}" -filter_complex "scale={VIDEO_SCALE}" -r {VIDEO_FPS} -c:v {VIDEO_CODEC} -pix_fmt {VIDEO_PIXEL_FORMAT} -b:v {VIDEO_BITRATE} -crf {VIDEO_CRF} -preset {VIDEO_PRESET} -c:a {VIDEO_AUDIO_CODEC} -b:a {VIDEO_AUDIO_BITRATE} -ac {VIDEO_AUDIO_CHANNELS} -ar {VIDEO_AUDIO_SAMPLE_RATE} -profile:v {VIDEO_PROFILE} -map_metadata -1 "{temp_filename}"', shell=True, check=True)
    message.reply_video(temp_filename)
    os.remove(file)
    os.remove(temp_filename)

app.run()
