from tkinter import *
from tkinter import ttk
from tkinter import font

from minizinc import Instance, Model, Solver

def generate(*args):
    try:
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score.get())
        # Solve and print solution
        result = instance.solve()
        solution.set(result["partie"])
    except ValueError:
        pass

def complete(*args):
    try:
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score2.get())
        instance["partie"] = int(partie.get())
        # Solve and print solution
        result = instance.solve()
        solution2.set(result["partie"])
    except ValueError:
        pass

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
frame1 = ttk.Labelframe(mainframe, text='Générer une partie à partir d\'un score', padding="3 3 12 12")
frame1.grid(column=0, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

frame1score = ttk.Frame(frame1, padding="3 3 3 3")
frame1score.grid(column=0, row=0, sticky=(N, W, E, S))
frame1solution = ttk.Frame(frame1, padding="3 3 3 3")
frame1solution.grid(column=0, row=1, sticky=(N, W, E, S))
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

score = StringVar()
score_entry = ttk.Entry(frame1score, width=10, textvariable=score)
score_entry.grid(column=1, row=0, sticky=(W, E))

solution = StringVar()
ttk.Label(frame1solution, width=50, textvariable=solution).grid(column=1, row=1, sticky=(W, E))

ttk.Button(frame1score, text="Valider", command=generate).grid(column=2, row=0, sticky=W)

ttk.Label(frame1score, text="Score :").grid(column=0, row=0, sticky=W)
ttk.Label(frame1solution, text="La réponse est :").grid(column=0, row=1, sticky=W)

# Part 2 : Complete a given partie
frame2 = ttk.Labelframe(mainframe, text='Compléter une partie', padding="3 3 12 12")
frame2.grid(column=0, row=2, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

frame2score = ttk.Frame(frame2, padding="3 3 3 3")
frame2score.grid(column=0, row=0, sticky=(N, W, E, S))
frame2partie = ttk.Frame(frame2, padding="3 3 3 3")
frame2partie.grid(column=0, row=1, sticky=(N, W, E, S))
frame2solution = ttk.Frame(frame2, padding="3 3 3 3")
frame2solution.grid(column=0, row=2, sticky=(N, W, E, S))
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

score2 = StringVar()
score_entry2 = ttk.Entry(frame2score, width=10, textvariable=score2)
score_entry2.grid(column=1, row=0, sticky=(W, E))

partie = StringVar()
partie_entry = ttk.Entry(frame2partie, width=50, textvariable=partie)
partie_entry.grid(column=1, row=1, sticky=(W, E))

solution2 = StringVar()
ttk.Label(frame2solution, width=50, textvariable=solution2).grid(column=1, row=2, sticky=(W, E))

ttk.Button(frame2partie, text="Valider", command=complete).grid(column=2, row=1, sticky=W)

ttk.Label(frame2score, text="Score :").grid(column=0, row=0, sticky=W)
ttk.Label(frame2partie, text="Partie incomplète :").grid(column=0, row=1, sticky=W)
ttk.Label(frame2solution, text="La réponse est :").grid(column=0, row=2, sticky=W)
    
for child in frame1score.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
for child in frame1solution.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
for child in frame2score.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
for child in frame2partie.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
for child in frame2solution.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

score_entry.focus()
root.bind("<Return>", generate)

root.mainloop()
