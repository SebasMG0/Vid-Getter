#ignore-warnings
from pydub import AudioSegment
import os

#AudioSegment.converter = r"ffmpeg-win/bin/ffmpeg.exe"

def m4a_to_mp3(path, file):
    """Converts an M4A audio file to MP3 format.

    Args:
        m4a_file (str): Path to the input M4A file.
        mp3_file (str): Path to the output MP3 file.
    """
    audio = AudioSegment.from_file(path/(file+".m4a"), format="m4a")
    audio.export(path/(file+".mp3"), format="mp3")
    os.remove(path/(file+".m4a"))