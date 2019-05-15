menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

menubar.add_casecade(label='File', menu = filemenu)
filemenu.add_command(label='Open', command = open_file)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = Exit)


Rooot.confi(menu=menubar)
