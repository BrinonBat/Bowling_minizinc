from tkinter.constants import NONE
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


def complete(nb_fails,nb_spares,nb_strikes,solution,score,partie):
    try:
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score.get())
        if partie!=NONE: instance["init"] = EntryToValue(partie)
        else: instance["init"] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
        # Solve and print solution
        result = instance.solve()
        """
        if result.status==Status.SATISFIED:
            solution.set(result["partie"])
        else :
            solution.set("UNSATISFIABLE")
        """

        solution.set(result["partie"])
        
        nb_fails = result["nb_fails"]
        nb_spares = result["nb_spares"]
        nb_strikes = result["nb_strikes"]

        print(" il y a "+str(nb_fails)+" echecs, "+str(nb_spares)+" spares et "+str(nb_strikes)+" strikes ")
        

        
    
    except ValueError:
        pass
