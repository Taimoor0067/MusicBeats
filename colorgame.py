import tkinter
import random
#list of color
colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange', 'white', 'purple', 'brown']
score = 0
time_left = 45
def startGame(event):
    if time_left == 45:
        count_down()
        next_color()
