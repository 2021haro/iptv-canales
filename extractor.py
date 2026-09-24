# Lista IPTV definitiva con Las Estrellas, N+ y canales estables
contenido_m3u = """#EXTM3U
#EXTINF:-1,Las Estrellas
https://channel01-onlymex.akamaized.net/hls/live/2022749/event01/index.m3u8

#EXTINF:-1 tvg-logo="https://i.imgur.com/TwBa344.png" group-title="Informativos", N+ (Nacional)
https://nomvauth.univision.com/api/v3/akamai-auth/token-auth?url=https://channel07secure.akamaized.net/hls/live/2036971-b/event01/index.m3u8&redirect=true

#EXTINF:-1 tvg-logo="https://i.imgur.com/dDFrONz.png" group-title="Informativos", N+ Foro (Televisa) (Nacional)
https://notusaauth.univision.com/api/v3/akamai-auth/token-auth?url=https://channel02secure-notusa.akamaized.net/hls/live/2023914-b/event01/index.m3u8&redirect=true

#EXTINF:-1 tvg-logo="https://i.imgur.com/TwBa344.png" group-title="Informativos", N+ Monterrey (Nuevo León)
https://notusaauth.univision.com/api/v3/akamai-auth/token-auth?url=https://channel09secure-notusa.akamaized.net/hls/live/2094418-b/event01/index.m3u8&redirect=true

#EXTINF:-1 tvg-logo="https://i.imgur.com/IrimbhT.png" group-title="Informativos", N+ Guadalajara (Jalisco)
https://notusaauth.univision.com/api/v3/akamai-auth/token-auth?url=https://channel08secure-notusa.akamaized.net/hls/live/2037034-b/event01/index.m3u8&redirect=true

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
#EXTINF:-1,RCG Noticias Saltillo
https://video1.getstreamhosting.com:1936/8172/8172/chunklist_w961798368.m3u8
#EXTINF:-1,Teleritmo
https://mdstrm.com/live-stream-playlist/57b4dc126338448314449d0c.m3u8
#EXTINF:-1,CGTN Español
https://mdstrm.com/live-stream-playlist/60b578b060947317de7b57ac.m3u8
#EXTINF:-1,RT TV Español
https://rt-esp.rttv.com/dvr/rtesp/playlist_800Kb.m3u8
#EXTINF:-1,DW Español
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1,Telefórmula
https://mdstrm.com/live-stream-playlist/62f2c855f7981b5a5a2d8763.m3u8
#EXTINF:-1,adn40 Noticias
https://mdstrm.com/live-stream-playlist/60b578b060947317de7b57ac.m3u8
#EXTINF:-1,Canal Once CDMX
https://vivo.canaloncelive.tv/secureoncedos/oncedigital/chunklist.m3u8
#EXTINF:-1,Canal del Congreso (45.1)
https://ccstreaming.packet.mx/WebRTCAppEE/streams/45.1_kd5oiNTTWO0gEOFc431277834_480p1000kbps.m3u8
#EXTINF:-1,Canal del Congreso (45.2)
https://ccstreaming.packet.mx/WebRTCAppEE/streams/45.2_kd5oiNTTWO0gEOFc423456787er_480p1000kbps.m3u8
#EXTINF:-1,Canal del Congreso (45.3)
https://ccstreaming.packet.mx/WebRTCAppEE/streams/45.3_kd5oiNTTWO0gEOFc875423kf52.m3u8
"""

# Guardamos el resultado en playlist.m3u
with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_m3u)

print("¡Archivo playlist.m3u actualizado con DW (Índice Maestro) con éxito!")
