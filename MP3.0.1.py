import mp3play
import tkfiledialog
import Tkinter


def open_file():
    global music
    global mp3
    global play_list
    filename.set(tkfiledialog.askopenfilename(defaultextension = "mp3" , filetypes = [("All types", ".*"), ("MP3", "mp3")]))
    playlist = filename.get()
    playlist_pieces = playlist.split("/")
    play_list.set(playlist_pieces[- 1])
    play1 = play_list.get()
    play_list_display.insert(END, play1)
    mp3 = filename.get()
    print(mp3)
    music = mp3play.load(mp3)
    pieces = mp3.split("/")
    name.set (pieces[- 1 ])
