from pytubefix import YouTube
from pytubefix.cli import on_progress
import converter

def download_m4a(url:str, path:str):
    yt = YouTube(url, on_progress_callback=on_progress)
    
    print("*"*63)
    print("\tDescargando: ", yt.title)

    ys = yt.streams.get_audio_only()
    ys.download(output_path=path, filename=yt.title+".m4a")
    converter.m4a_to_mp3(path, yt.title)
    
    print("\n","*"*63)

    return yt.title

def download_serie(serie:list[str], path):
    for url in serie:
        try:
            download_m4a(url.strip(), path)

        except Exception as e:
            print(f"Error al descargar {url}: {e}")

    print("\tSerie de descargas finalizada.")