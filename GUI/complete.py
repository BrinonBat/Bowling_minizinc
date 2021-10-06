from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from minizinc import Instance, Model, Solver

# servira a verifier si x est valide avant de l'envoyer à minizinc


def is_ok(x):
    try:
        x = int(x)
        if(x >= 0 and x <= 10):
            return True
        return False
    except:
        return False

# convertion de la liste de saisie String en liste d'Int utilisable par minizinc


def entryToValue(entries):
    entry_values = []

    for i in range(0, 21):
        if(entries[i].get()):
            if is_ok(entries[i].get()):
                entry_values.append(int(entries[i].get()))
            else:
                print(
                    "error : please select a number between 0 and 10 at indice "+i)
                entry_values.append(-1)
        else:
            entry_values.append(-1)

    return entry_values


def complete(self, score, partie):
    try:
        print(score)
        print(partie)
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score)
        instance["init"] = entryToValue(partie)
        print(entryToValue(partie))
        # Solve and print solution
        result = instance.solve()
        """
        if result.status==Status.SATISFIED:
            solution.set(result["partie"])
        else :
            solution.set("UNSATISFIABLE")
        """

        self.current_screen.solution_generee.text = result["partie"]
        print(result["partie"])
    except ValueError:
        pass

    self.current_screen.label_solution_generee.opacity = 1
    self.current_screen.solution_generee.opacity = 1


class CompleteWindow(Screen):
    pass
