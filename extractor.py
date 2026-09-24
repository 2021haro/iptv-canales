import time
from playwright.sync_api import sync_playwright

# Diccionario con los canales y sus páginas web oficiales
canales = {
    "Canal 6 Monterrey": "https://www.multimediostv.com/en-vivo/monterrey",
    "Canal 6 Saltillo": "https://www.multimediostv.com/en-vivo/saltillo",
    "Canal 6 CDMX": "https://www.multimediostv.com/en-vivo/cdmx"
}

enlaces_capturados = []

with sync_playwright() as p:
    # Iniciamos el navegador en modo invisible para la nube
    browser = p.chromium.launch(headless=True)
    
    for nombre, url in canales.items():
        print(f"Analizando: {nombre}...")
        context = browser.new_context()
        page = context.new_page()
        
        # Usamos un diccionario para almacenar el estado y evitar problemas de scope
        estado = {"stream_url": None}

        # Función para interceptar las peticiones de red del reproductor
        def capturar_red(request):
            req_url = request.url
            # Buscamos los patrones característicos de streaming HLS/Dash
            if ".m3u8" in req_url or "manifest" in req_url:
                if "cdn.mdstrm.com" in req_url or "live" in req_url:
                    estado["stream_url"] = req_url

        page.on("request", capturar_red)

        try:
            # Navegamos a la web del canal
            page.goto(url, timeout=50000)
            # Damos unos segundos para que el reproductor cargue los tokens dinámicos
            time.sleep(12)
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
