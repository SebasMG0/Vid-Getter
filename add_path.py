import os
import sys

def obtener_ruta_ffmpeg():
    if getattr(sys, 'frozen', False):
        # Si está empaquetado con PyInstaller
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, "ffmpeg", "bin", "ffmpeg.exe")

def add_ffmpeg_to_path():
    """
    Agrega la ruta de ffmpeg al PATH del sistema.
    """
    ffmpeg_path = obtener_ruta_ffmpeg()
    if os.path.exists(ffmpeg_path):
        os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
    else:
        raise FileNotFoundError(f"No se encontró ffmpeg en la ruta: {ffmpeg_path}")
