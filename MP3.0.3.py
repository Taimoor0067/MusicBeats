def vol(event):
    v = Scale.get(volume_slider)
    music.volume(v)

def Exit():
    exit()


root = Tk()
root.title("Ickle Music Player")
root.geometry("400*200+350+200")
filename = Tkinter.stringVar()
name = Tkinter.stringVar()
play_list = Tkinter.stringVar()
