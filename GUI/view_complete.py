from tkinter import *
from tkinter import ttk
from tkinter import font
from minizinc import Instance, Model, Solver, Status

#servira a verifier si x est valide avant de l'envoyer à minizinc
def is_ok(x):
    try:
        x = int(x)
        if(x>=0 and x<=10): return True
        return False
    except:
        return False

#convertion de la liste de saisie String en liste d'Int utilisable par minizinc
def EntryToValue(entries):
    entry_values=[]

    for i in range (0,21):
        if(entries[i].get()):
            if is_ok(entries[i].get()):
                entry_values.append(int(entries[i].get()))
            else :
                print("error : please select a number between 0 and 10 at indice "+i)
                entry_values.append(-1)
        else :
            entry_values.append(-1)
    
    return entry_values

def complete(solution,score,partie):
    try:
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score.get())
        instance["init"] = EntryToValue(partie)
        print(EntryToValue(partie))
        # Solve and print solution
        result = instance.solve()
        if result.status==Status.SATISFIED:
            solution.set(result["partie"])

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

    solution2 = StringVar()
    ttk.Label(frame2solution, width=50, textvariable=solution2).grid(column=1, row=3, sticky=(W, E))

    ttk.Button(frame2solution, text="Valider", command=lambda: complete(solution2,score2,entries)).grid(column=1, row=1, sticky=W)
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
