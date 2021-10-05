from tkinter import *
from tkinter import ttk
from tkinter import font

from minizinc import Instance, Model, Solver

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
    
def PrintWindow(mainframe):
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

    dig1 = StringVar()
    dig1_entry = ttk.Entry(frame2partie, width=1, textvariable=dig1)
    dig1_entry.grid(column=1, row=1, sticky=(W, E))

    dig2 = StringVar()
    dig2_entry = ttk.Entry(frame2partie, width=1, textvariable=dig2)
    dig2_entry.grid(column=2, row=1, sticky=(W, E))

    ttk.Label(frame2partie,text="|").grid(column=3, row=1, sticky=(W, E))

    dig3 = StringVar()
    dig3_entry = ttk.Entry(frame2partie, width=1, textvariable=dig3)
    dig3_entry.grid(column=4, row=1, sticky=(W, E))

    dig4 = StringVar()
    dig4_entry = ttk.Entry(frame2partie, width=1, textvariable=dig4)
    dig4_entry.grid(column=5, row=1, sticky=(W, E))

    ttk.Label(frame2partie,text="|").grid(column=6, row=1, sticky=(W, E))

    dig5 = StringVar()
    dig5_entry = ttk.Entry(frame2partie, width=1, textvariable=dig5)
    dig5_entry.grid(column=7, row=1, sticky=(W, E))

    dig6 = StringVar()
    dig6_entry = ttk.Entry(frame2partie, width=1, textvariable=dig6)
    dig6_entry.grid(column=8, row=1, sticky=(W, E))

    ttk.Label(frame2partie,text="|").grid(column=9, row=1, sticky=(W, E))

    dig7 = StringVar()
    dig7_entry = ttk.Entry(frame2partie, width=1, textvariable=dig7)
    dig7_entry.grid(column=10, row=1, sticky=(W, E))

    dig8 = StringVar()
    dig8_entry = ttk.Entry(frame2partie, width=1, textvariable=dig8)
    dig8_entry.grid(column=11, row=1, sticky=(W, E))

    solution2 = StringVar()
    ttk.Label(frame2solution, width=50, textvariable=solution2).grid(column=1, row=3, sticky=(W, E))

    ttk.Button(frame2solution, text="Valider", command=complete).grid(column=1, row=1, sticky=W)

    ttk.Label(frame2score, text="Score :").grid(column=0, row=0, sticky=W)
    ttk.Label(frame2partie, text="Partie incomplète :").grid(column=0, row=1, sticky=W)
    ttk.Label(frame2solution, text="La réponse est :").grid(column=0, row=2, sticky=W)

    for child in frame2score.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    for child in frame2partie.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    for child in frame2solution.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
