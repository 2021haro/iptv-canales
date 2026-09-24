import time
from playwright.sync_api import sync_playwright

# 1. Tus canales estables que ya tienes guardados (no necesitan abrir navegador)
canales_estables = [
    ("Canal 6 Monterrey", "https://mdstrm.com/live-stream-playlist/57b4dbf5dbbfc8f16bb63ce1.m3u8"),
    ("Canal 6 CDMX", "https://mdstrm.com/live-stream-playlist/5f2d9d6ff17144074bd8a284.m3u8"),
    ("Canal 6 Guadalajara", "https://mdstrm.com/live-stream-playlist/5c54d38ca392a5119bb0aa0d.m3u8"),
    ("Canal 6 Puebla", "https://mdstrm.com/live-stream-playlist/5d56ed29c92dd106ff01543b.m3u8"),
    ("Canal 6 Bajío", "https://mdstrm.com/live-stream-playlist/5d4b0fec848918070128c8cb.m3u8"),
    ("Canal 6 Laguna", "https://mdstrm.com/live-stream-playlist/57bf686a61ff39e1085d43e1.m3u8"),
    ("Canal 6 Saltillo", "https://mdstrm.com/live-stream-playlist/5d5d51a4e9a40e25f4a0332c.m3u8"),
    ("Teleritmo", "https://mdstrm.com/live-stream-playlist/57b4dc126338448314449d0c.m3u8"),
    ("CGTN Español", "https://mdstrm.com/live-stream-playlist/60b578b060947317de7b57ac.m3u8"),
    ("Telefórmula", "https://mdstrm.com/live-stream-playlist/62f2c855f7981b5a5a2d8763.m3u8")
]

# 2. Los canales de N+ que requieren esperar los anuncios de 1 a 2 minutos
canales_nmas = {
    "N+ ForoTV": "https://www.nmas.com.mx/en-vivo/?canal=forotv",
    "N+ Noticieros": "https://www.nmas.com.mx/en-vivo/?canal=noticieros",
    "N+ Guadalajara": "https://www.nmas.com.mx/en-vivo/?canal=guadalajara",
    "N+ Monterrey": "https://www.nmas.com.mx/en-vivo/?canal=monterrey"
}

# Empezamos la lista con los estables
enlaces_capturados = list(canales_estables)

with sync_playwright() as p:
    # Lanzamos el navegador invisible optimizado
    browser = p.chromium.launch(
        headless=True,
        args=["--autoplay-policy=no-user-gesture-required"]
    )
    
    for nombre, url in canales_nmas.items():
        print(f"Analizando {nombre} y esperando a que pasen los anuncios...")
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        estado = {"stream_url": None}

        def capturar_red(request):
            req_url = request.url
            # Buscamos los patrones de video en vivo (HLS o DASH)
            if ".m3u8" in req_url or "manifest" in req_url:
                if "akamaized.net" in req_url or "nmas" in req_url or "video" in req_url or "live" in req_url:
                    estado["stream_url"] = req_url

        page.on("request", capturar_red)

        try:
            page.goto(url, timeout=60000)
            time.sleep(5)
            
            # Intentamos hacer clic en el reproductor por si requiere interacción
            try:
                page.click("video, button, .jw-display-icon-container", timeout=5000)
            except:
                pass
                
            # Damos 80 segundos de margen para rebasar los anuncios de 1-2 minutos
            print(f"Esperando 80 segundos en {nombre} para capturar la señal post-anuncio...")
            time.sleep(80)
        except Exception as e:
            print(f"Error al procesar {nombre}: {e}")

        if estado["stream_url"]:
            print(f"[OK] Enlace obtenido para {nombre}")
            enlaces_capturados.append((nombre, estado["stream_url"]))
        else:
            print(f"[X] No se pudo capturar el enlace para {nombre}")
            
        context.close()

    browser.close()

# Construimos el archivo M3U unificado con absolutamente todos los canales
contenido_m3u = "#EXTM3U\n"
for nombre, link in enlaces_capturados:
    contenido_m3u += f"#EXTINF:-1,{nombre}\n{link}\n"

# Guardamos el resultado final en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Proceso finalizado! Archivo playlist.m3u unificado correctamente.")
