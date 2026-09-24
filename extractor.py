import time
from playwright.sync_api import sync_playwright

canales = {
    "Canal 6 Monterrey": "https://www.multimediostv.com/en-vivo/monterrey",
    "Canal 6 Saltillo": "https://www.multimediostv.com/en-vivo/saltillo",
    "Canal 6 CDMX": "https://www.multimediostv.com/en-vivo/cdmx"
}

enlaces_capturados = []

with sync_playwright() as p:
    # Lanzamos el navegador permitiendo autoplay sin restricciones de usuario
    browser = p.chromium.launch(
        headless=True,
        args=["--autoplay-policy=no-user-gesture-required"]
    )
    
    for nombre, url in canales.items():
        print(f"Analizando: {nombre}...")
        # Creamos un contexto simulando un navegador de PC real (User-Agent)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        estado = {"stream_url": None}

        def capturar_red(request):
            req_url = request.url
            # Filtro optimizado para capturar cualquier manifiesto de Mediastream
            if "mdstrm.com" in req_url and (".m3u8" in req_url or "manifest" in req_url or "playlist" in req_url):
                print(f"¡Enlace detectado!: {req_url}")
                estado["stream_url"] = req_url

        page.on("request", capturar_red)

        try:
            page.goto(url, timeout=60000)
            time.sleep(5)
            
            # Intentamos hacer clic en el reproductor por si requiere interacción para arrancar
            try:
                page.click("video, .play-button, .jw-display-icon-container, button", timeout=5000)
            except:
                pass
                
            print("Esperando a que pase la publicidad y cargue el streaming...")
            time.sleep(30)
        except Exception as e:
            print(f"Error al procesar {nombre}: {e}")

        if estado["stream_url"]:
            print(f"[OK] Enlace obtenido para {nombre}")
            enlaces_capturados.append((nombre, estado["stream_url"]))
        else:
            print(f"[X] No se pudo capturar el enlace para {nombre}")
            
        context.close()

    browser.close()

# Construimos el contenido del archivo M3U unificado
contenido_m3u = "#EXTM3U\n"
for nombre, link in enlaces_capturados:
    contenido_m3u += f"#EXTINF:-1,{nombre}\n{link}\n"

# Guardamos el resultado final en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Proceso finalizado! Archivo playlist.m3u actualizado correctamente.")
