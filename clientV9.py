import socket
import time
import vlc

media_player = vlc.MediaPlayer()
media = vlc.Media("synctest.mp4")
media_player.set_media(media)

host = '192.168.0.119'
port = 5050

for x in range(10):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("connected")
    except:
        print("couldn't connect")
        time.sleep(1)

media_player.play()
media_player.pause()

while True:
    msg = s.recv(16)
    print(msg.decode("utf-8"))
    msgD = msg.decode("utf-8")
    if msg == 0 or msgD == "restart":
        media_player.set_position(0.0001)
        print("to the beginning and beyond")
        media_player.play()
    else:
        media_player.play()


