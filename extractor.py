import requests

# Enlaces directos oficiales de los canales de Multimedios (Mediastream CDN)
canales = {
    "Canal 6 Monterrey": "https://mdstrm.com/live-stream-playlist/57b4dbf5dbbfc8f16bb63ce1.m3u8",
    "Canal 6 Saltillo": "https://mdstrm.com/live-stream-playlist/5d5d51a4e9a40e25f4a0332c.m3u8",
    "Canal 6 CDMX": "https://mdstrm.com/live-stream-playlist/5f2d9d6ff17144074bd8a284.m3u8"
}

enlaces_capturados = []

for nombre, url in canales.items():
    print(f"Verificando canal: {nombre}...")
    try:
        # Hacemos una petición rápida para confirmar que el servidor responde
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            print(f"[OK] {nombre} verificado correctamente.")
            enlaces_capturados.append((nombre, url))
        else:
            print(f"[X] {nombre} no disponible (Código {response.status_code})")
    except Exception as e:
        print(f"Error al conectar con {nombre}: {e}")

# Construimos el contenido del archivo M3U unificado
contenido_m3u = "#EXTM3U\n"
for nombre, link in enlaces_capturados:
    contenido_m3u += f"#EXTINF:-1,{nombre}\n{link}\n"

# Guardamos el resultado final en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Proceso finalizado! Archivo playlist.m3u actualizado correctamente.")
