import time
from urllib.parse import unquote
from playwright.sync_api import sync_playwright

# Canales estables (Se guardan de inmediato sin demoras)
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

# Canales de N+ que requieren saltar la publicidad
canales_nmas = {
    "N+ ForoTV": "https://www.nmas.com.mx/en-vivo/?canal=forotv",
    "N+ Noticieros": "https://www.nmas.com.mx/en-vivo/?canal=noticieros",
    "N+ Guadalajara": "https://www.nmas.com.mx/en-vivo/?canal=guadalajara",
    "N+ Monterrey": "https://www.nmas.com.mx/en-vivo/?canal=monterrey"
}

enlaces_capturados = list(canales_estables)

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--autoplay-policy=no-user-gesture-required"]
    )
    
    for nombre, url in canales_nmas.items():
        print(f"Extrayendo señal limpia de {nombre}...")
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        estado = {"stream_url": None}

        def capturar_red(request):
            req_url = request.url
            # Si detectamos el reporte de JW Player de N+ que contiene el link real dentro de 'mu='
            if "jwpltx.com" in req_url and "mu=" in req_url:
                try:
                    # Decodificamos la URL interna de la variable 'mu'
                    partes = req_url.split("mu=")
                    if len(partes) > 1:
                        link_interno = partes[1].split("&")[0]
                        link_limpio = unquote(link_interno)
                        if ".m3u8" in link_limpio:
                            estado["stream_url"] = link_limpio
                except:
                    pass
            # O si el reproductor hace petición directa a un m3u8 de akamai
            elif ".m3u8" in req_url and "akamaized.net" in req_url:
                if estado["stream_url"] is None:
                    estado["stream_url"] = req_url

        page.on("request", capturar_red)

        try:
            page.goto(url, timeout=60000)
            time.sleep(5)
            try:
                page.click("video, button, .jw-display-icon-container", timeout=5000)
            except:
                pass
                
            # Esperamos 50 segundos para superar los anuncios y capturar el token fresco
            time.sleep(50)
        except Exception as e:
            print(f"Error al procesar {nombre}: {e}")

        if estado["stream_url"]:
            print(f"[OK] Enlace limpio obtenido para {nombre}")
            enlaces_capturados.append((nombre, estado["stream_url"]))
        else:
            print(f"[X] No se pudo capturar el enlace para {nombre}")
            
        context.close()

    browser.close()

# Construimos el archivo M3U final unificado
contenido_m3u = "#EXTM3U\n"
for nombre, link in enlaces_capturados:
    contenido_m3u += f"#EXTINF:-1,{nombre}\n{link}\n"

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Archivo playlist.m3u generado con enlaces limpios y correctos!")
