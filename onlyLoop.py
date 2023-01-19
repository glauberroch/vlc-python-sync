import time
import vlc

media_player = vlc.MediaPlayer()
media = vlc.Media("synctest.mp4")
media_player.set_media(media)

while True:
    media_player.play()
    videoPos = media_player.get_position()
    print(videoPos)
    if videoPos >= 0.2:
        media_player.set_position(0.00001)