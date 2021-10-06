from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from minizinc import Instance, Model, Solver


def convert_to_string(partie):
    string = ""
    for i in range(len(partie)):
        if i % 2 == 0:
            string += "|"
        string += str(partie[i]) + " "
    return string


def generate(self, score):
    try:
        # Load model from file
        model = Model("brouillon_model.mzn")
        # Find the MiniZinc solver configuration for Gecode
        gecode = Solver.lookup("gecode")
        # Create an Instance of the model for Gecode
        instance = Instance(gecode, model)
        # Assign values
        instance["score_total"] = int(score)
        instance["init"] = [-1, -1, -1, -1, -1, -1, -1, -1, -
                            1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        # Solve and print solution
        result = instance.solve()
        self.current_screen.solution_generee.text = convert_to_string(
            result["partie"])
    except ValueError:
        pass

    self.current_screen.label_solution_generee.opacity = 1
    self.current_screen.solution_generee.opacity = 1


class ScoreWindow(Screen):
    pass
