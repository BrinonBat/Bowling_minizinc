from tkinter import *
from tkinter import ttk
from tkinter import font
import view_complete
import view_score
from minizinc import Instance, Model, Solver

# Title of the window
root = Tk()
root.title("Bowling !")

# MainFrame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create Fonts
titleFont = font.Font(family='Helvetica', name='titleFont', size=16, weight='normal')
subtitleFont = font.Font(family='Helvetica', name='subtitleFont', size=14, weight='normal')
textFont = font.Font(family='Helvetica', name='textFont', size=12, weight='normal')

# Create title "Bowling !"
ttk.Label(mainframe, text='Bowling !', font=titleFont).grid(column=0, row=0, sticky=N)

# Part 1 : Generate partie with given score
view_score.PrintWindow(mainframe)

# Part 2 : Complete a given partie
view_complete.PrintWindow(mainframe)
    
#score_entry.focus()
#root.bind("<Return>", generate)

root.mainloop()
