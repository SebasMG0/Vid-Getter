from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_m4a(url:str):
    yt = YouTube(url, on_progress_callback=on_progress)
    
    print("*"*63)
    print("\tDescargando: ", yt.title)

    ys = yt.streams.get_audio_only()
    ys.download()
    
    print("\n","*"*63)

    return yt.title

def download_serie(serie:list[str]):
    for url in serie:
        try:
            download_m4a(url.strip())

        except Exception as e:
            print(f"Error al descargar {url}: {e}")

    print("\tSerie de descargas finalizada.")