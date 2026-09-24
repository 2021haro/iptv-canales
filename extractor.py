# Contenido de la lista IPTV con los enlaces oficiales estables
contenido_m3u = """#EXTM3U
#EXTINF:-1,Canal 6 Monterrey
https://mdstrm.com/live-stream-playlist/57b4dbf5dbbfc8f16bb63ce1.m3u8
#EXTINF:-1,Canal 6 CDMX
https://mdstrm.com/live-stream-playlist/5f2d9d6ff17144074bd8a284.m3u8
#EXTINF:-1,Canal 6 Laguna
https://mdstrm.com/live-stream-playlist/57bf686a61ff39e1085d43e1.m3u8
"""

# Guardamos el resultado en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Archivo playlist.m3u generado y actualizado correctamente!")
