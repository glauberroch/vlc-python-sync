#V8 Trying to loop and send message to client when it starts

import socket
import time
import vlc

media_player = vlc.MediaPlayer()
media = vlc.Media("synctest.mp4")
media_player.set_media(media)

host = ''
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

#media_player.play()
#media_player.pause()

while True:
    
    clientsocket, address = s.accept()
    print(f"connection established")
    
    media_player.play()
    videoPos = media_player.get_position()
    print(videoPos)

    if videoPos >= 0.999:
        media_player.set_position(0.0001)
        print("end")   
        clientsocket.send(bytes("restart","utf-8"))
        print("start again!")

