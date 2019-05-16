open_file = Button(root, width = 8, height = 2, text = 'open file', command = open_file)
open_file.grid(row=1, column=4)

play_button = Button(root, width = 6, height = 3, text='Play', command = play)
play_button .grid(row=1, column=2, sticky = w)

stop_button = Button(root, width = 6, height = 3, text = 'Stop', command=stop)
stop_button.grid(row=1, column=2, sticky = w)

pause_button = Button(root, width = 6, height = 3, text = 'Pause', command=pause)
pause_button.grid(row=1, column=3)
