from tkinter import *
from tkinter import ttk
from minizinc import Instance, Model, Solver
import interface_mzn


def PrintWindow(mainframe):
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

    nb_fails=0
    nb_spares=0
    nb_strikes=0

    score = StringVar()
    score_entry = ttk.Entry(frame1score, width=10, textvariable=score)
    score_entry.grid(column=1, row=0, sticky=(W, E))

    solution = StringVar()
    ttk.Label(frame1solution, width=50, textvariable=solution).grid(column=1, row=1, sticky=(W, E))

    ttk.Button(frame1score, text="Valider", command=lambda: interface_mzn.complete(nb_fails,nb_spares,nb_strikes,solution,score,NONE)).grid(column=2, row=0, sticky=W)

    ttk.Label(frame1score, text="Score :").grid(column=0, row=0, sticky=W)
    ttk.Label(frame1solution, text="La réponse est :").grid(column=0, row=1, sticky=W)

    for child in frame1score.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    for child in frame1solution.winfo_children(): 
        child.grid_configure(padx=5, pady=5)