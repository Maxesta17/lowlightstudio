import os
import requests

def download_missing_assets():
    # Estructura de carpetas necesaria
    assets = {
        "sound": ["https://studiolumio.com/sound/ambient-space.mp3"],
        "video": ["https://r2.studiolumio.com/lumio-reel.mp4"],
        "_next/static/media": [
            "https://studiolumio.com/_next/static/media/35415d5027fd8570-s.p.woff2",
            "https://studiolumio.com/_next/static/media/cee54c58f389a0a9-s.p.woff2",
            "https://studiolumio.com/_next/static/media/028c0d39d2e8f589-s.p.woff2"
        ]
    }

    print("[*] Iniciando descarga de activos pesados...")

    for folder, urls in assets.items():
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        for url in urls:
            filename = os.path.join(folder, url.split('/')[-1])
            print(f"[*] Descargando: {url} -> {filename}")
            try:
                r = requests.get(url, stream=True)
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk: f.write(chunk)
                print(f"[+] Completado: {filename}")
            except Exception as e:
                print(f"[!] Error descargando {url}: {e}")

    print("\n[FIN] Todos los activos críticos han sido recuperados.")

download_missing_assets()