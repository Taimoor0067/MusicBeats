def play():
    music.play()

def stop():
    music.stop()

def pause():
    if music.ispaused() == True :
        music.unpaused()
    else music.ispaused() == False:
        music.pause()
