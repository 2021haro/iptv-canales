# Contenido completo de la lista IPTV unificada con los canales estables
contenido_m3u = """#EXTM3U
#EXTINF:-1,Canal 6 Monterrey
https://mdstrm.com/live-stream-playlist/57b4dbf5dbbfc8f16bb63ce1.m3u8
#EXTINF:-1,Canal 6 CDMX
https://mdstrm.com/live-stream-playlist/5f2d9d6ff17144074bd8a284.m3u8
#EXTINF:-1,Canal 6 Guadalajara
https://mdstrm.com/live-stream-playlist/5c54d38ca392a5119bb0aa0d.m3u8
#EXTINF:-1,Canal 6 Puebla
https://mdstrm.com/live-stream-playlist/5d56ed29c92dd106ff01543b.m3u8
#EXTINF:-1,Canal 6 Bajío
https://mdstrm.com/live-stream-playlist/5d4b0fec848918070128c8cb.m3u8
#EXTINF:-1,Canal 6 Laguna
https://mdstrm.com/live-stream-playlist/57bf686a61ff39e1085d43e1.m3u8
#EXTINF:-1,Canal 6 Saltillo
https://mdstrm.com/live-stream-playlist/5d5d51a4e9a40e25f4a0332c.m3u8
#EXTINF:-1,Teleritmo
https://mdstrm.com/live-stream-playlist/57b4dc126338448314449d0c.m3u8
#EXTINF:-1,CGTN Español
https://mdstrm.com/live-stream-playlist/60b578b060947317de7b57ac.m3u8
"""

# Guardamos el resultado en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Archivo playlist.m3u actualizado con todos los canales correctamente!")
