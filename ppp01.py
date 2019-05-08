# Countdown timer function
def count_down():
    global time_left
if time_left > 0:
    time_left -= 1
    timelabel.config(text = "time left" + str('time_left'))
    timelabel.after(2000,count_down)                
