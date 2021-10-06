from tkinter import *
from tkinter import ttk
import interface_mzn



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

    nb_fails=0
    nb_spares=0
    nb_strikes=0

    solution2 = StringVar()
    ttk.Label(frame2solution, width=50, textvariable=solution2).grid(column=1, row=3, sticky=(W, E))

    ttk.Button(frame2solution, text="Valider", command=lambda: interface_mzn.complete(nb_fails,nb_spares,nb_strikes,solution2,score2,entries)).grid(column=1, row=1, sticky=W)
    #ttk.Button(frame2solution, text="Test", command=lambda: test(solution2,entries)).grid(column=1, row=1, sticky=W)

    ttk.Label(frame2score, text="Score :").grid(column=0, row=0, sticky=W)
    ttk.Label(frame2partie, text="Partie incomplète :").grid(column=0, row=1, sticky=W)
    ttk.Label(frame2solution, text="La réponse est :").grid(column=0, row=2, sticky=W)

    entries=[]
    index_row=1
    index_col=1

    for i in range(0,21):
        entries.append(ttk.Entry(frame2partie, width=2))
        entries[i].grid(column=index_col, row=index_row, sticky=(W, E))
        index_col+=1

        ## ajouter ici condition : si entries[i-1]==10, alors entries[i] peut pas être saisi

        if not (index_col%3):
            ttk.Label(frame2partie,text="|").grid(column=index_col, row=index_row, sticky=(W, E))
            index_col+=1


    for child in frame2score.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    for child in frame2partie.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    for child in frame2solution.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
