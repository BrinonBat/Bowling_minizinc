from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from kivy.uix.button import Button


from minizinc import Instance, Model, Solver

from menu import *
from score import *
from complete import *

# Convertit un tableau d'entiers en string


def convert_to_string(partie):
    string = ""
    for i in range(len(partie)):
        if i % 2 == 0:
            string += "| "
        string += str(partie[i]) + " "
    return string

# Servira a verifier si x est valide avant de l'envoyer à minizinc


def is_ok(x):
    try:
        x = int(x)
        if(x >= 0 and x <= 10):
            return True
        return False
    except:
        return False

# Convertion de la liste de saisie String en liste d'Int utilisable par minizinc


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


class WindowManager(ScreenManager):

    def build(self):
        # Image de fond
        self.canvas.add(
            Rectangle(size=(1414, 1080), source='images/bowling_wallpaper.jpg'))
        self.canvas.add(Color(0, 0, 0, .4))
        self.canvas.add(Rectangle(size=(1414, 1080)))

        # Chargement de la vue Menu
        menuWindow = MenuWindow.build(self)
        self.add_widget(menuWindow)
        self.current = "menu_window"

        # Chargement de la vue Générer une partie
        scoreWindow = ScoreWindow.build(self)
        self.add_widget(scoreWindow)

        # Chargement de la vue Compléter une partie
        completeWindow = CompleteWindow.build(self)
        self.add_widget(completeWindow)

    def load_menu_window(self, button):
        self.current = "menu_window"
        self.transition.direction = "right"

    def load_score_window(self, button):
        self.current = "score_window"
        self.transition.direction = "left"

    def load_complete_window(self, button):
        self.current = "complete_window"
        self.transition.direction = "left"

    # def generate(self, score):
    #   self.complete(score, None)

    # def complete(self, score, partie):

    def complete(self, button):
        try:
            print(self.current_screen)
            if self.current_screen == "score_window":
                score = self.ids.view_score_input_score.text
                partie = [-1, -1, -1, -1, -1, -1, -1, -1, -
                          1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            else:
                score = self.ids.view_complete_input_score.text
                partie = self.ids.view_complete_input_partie.text

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
            if partie != None:
                instance["init"] = entryToValue(partie)
            else:
                instance["init"] = [-1, -1, -1, -1, -1, -1, -1, -1, -
                                    1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

            # Solve and print solution
            result = instance.solve()
            """
            if result.status==Status.SATISFIED:
                solution.set(result["partie"])
            else :
                solution.set("UNSATISFIABLE")
            """

            if self.current_screen == "score_window":
                self.ids.view_score_solution_generee.text = convert_to_string(
                    result["partie"])
                self.ids.view_score_label_solution_generee.opacity = 1
                self.ids.view_score_solution_generee.opacity = 1
            else:
                self.ids.view_complete_solution_generee.text = convert_to_string(
                    result["partie"])
                self.ids.view_complete_label_solution_generee.opacity = 1
                self.ids.view_complete_solution_generee.opacity = 1

            nb_fails = result["nb_fails"]
            nb_spares = result["nb_spares"]
            nb_strikes = result["nb_strikes"]

            print(" il y a "+str(nb_fails)+" echecs, "+str(nb_spares) +
                  " spares et "+str(nb_strikes)+" strikes ")

        except ValueError:
            pass


Config.set('graphics', 'width', '1414')
Config.set('graphics', 'height', '1080')

#kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        root = WindowManager()
        root.build()
        return root
        # return kv


MainApp().run()
