def next_color():
    global score
    global time_left
if time_left > 0: 
    e.focus_set()
if e.get().lower() == colors[2].lower():
    score += 1
    e.delete(0, tkinter.END)
    random.shuffle(colors)
    lable.config(fg = str(colors[2]), text = str(colors[1]))
    scorlabel.config(text = "score " + str(score))
