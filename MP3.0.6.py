volume_slide = Scale(root, label='volume', orient = 'horizontal', fg = 'red', command = vol)
volume_slide.grid(row=1, column=3)

file_name_label = Label(root, font=('audio song'), fg='red', wraplength = 350, textvariable=name)
file_name_label.grid(row=4, column=1, columnspan=10)

play_list_window = Toplevel(root, height = 170, width = 120)
play_list_window.title('Playlist')

play_list_display = Listbox(play_list_window, width = 70)
play_list_display.pack()

play_list_window.mainloop()
root.mainloop()
