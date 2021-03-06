import os
# os.environ['KIVY_GL_BACKEND']="sdl2"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from kivy.graphics import Color
from kivy.graphics import Rectangle
from datetime import timedelta

from minizinc import Instance, Model, Solver
from menu import *
from score import *
from complete import *

# Convertit un tableau d'entiers en string


def convert_to_string(partie):
    string = ""
    i = 0
    while i < 20:
        if i % 2 == 0 or i == 21:
            string += "| "
            if(i < 18):
                if (partie[i] == 10):
                    string += str(partie[i]) + " X "
                    i += 1
                elif (partie[i]+partie[i+1] == 10):
                    string += str(partie[i]) + " / "
                    i += 1
                else:
                    string += str(partie[i]) + " "
            else:
                if (partie[18] == 10):
                    string += str(partie[i])+" " + \
                        str(partie[i+1])+" | "+str(partie[i+2])
                    i += 3
                else:
                    string += str(partie[i]) + " "
        else:
            string += str(partie[i]) + " "
        i += 1
    return string + "|"

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
        if(entries[i]):
            if is_ok(entries[i]):
                entry_values.append(int(entries[i]))
            else:
                entry_values.append(-1)
        else:
            entry_values.append(-1)

    return entry_values


class WindowManager(ScreenManager):
    results = []
    sol_number = 0
    max_sol_number = 100
    solveChoice = "satisfy"

    def build(self):
        # Image de fond
        self.canvas.add(
            Rectangle(size=(1414, 1080), source='images/bowling_wallpaper.jpg'))
        self.canvas.add(Color(0, 0, 0, .4))
        self.canvas.add(Rectangle(size=(1414, 1080)))

        Window.size = (1410, 1080)

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

    def quit(self, button):
        App.get_running_app().stop()

    def complete(self, button):
        self.sol_number = 0
        self.max_sol_number = 1
        self.results = []
        self.solveChoice = "satisfy"

        try:
            erreur_saisie = False
            text_erreur = ""
            score = 0
            partie = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -
                      1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            if self.current_screen.name == 'score_window':
                if self.ids.view_score_input_score.text:
                    score = self.ids.view_score_input_score.text
                    self.solveChoice = self.ids.score_button_choice_solve.text
            else:
                if self.ids.view_complete_input_score.text:
                    self.solveChoice = self.ids.complete_button_choice_solve.text
                    score = self.ids.view_complete_input_score.text
                tab = self.ids.view_complete_input_partie
                for i in range(0, 21):
                    if tab[i].text:
                        if is_ok(tab[i].text):
                            partie[i] = int(tab[i].text)
                        else:
                            erreur_saisie = True
                            text_erreur = "Saisissez un nombre compris entre 0 et 10 au lancer numéro " + \
                                str(i + 1) + "."

            if erreur_saisie == False:
                for i in range(0, 20):
                    if i % 2 == 0 and partie[i] + partie[i + 1] > 10:
                        erreur_saisie = True
                        text_erreur = "Deux lancers consécutifs ne peuvent pas valoir plus de 10."

            if int(score) > 300:
                erreur_saisie = True
                text_erreur = "Vous ne pouvez pas dépasser le score de 300 points."
            if int(score) < 0:
                erreur_saisie = True
                text_erreur = "Vous ne pouvez pas avoir un score négatif."

            if erreur_saisie == False:
                # Load model from file
                model = Model("model.mzn")

                # ajout de la ligne solve en fonction de la selection de l'utilisateur
                if(self.solveChoice == "satisfy"):
                    model.add_string(
                        "\n solve::int_search(partie, first_fail, indomain_max,complete) satisfy;")
                    self.max_sol_number = 100
                elif(self.solveChoice == "maximize strikes"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) maximize(nb_strikes)")
                elif(self.solveChoice == "minimize strikes"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) minimize(nb_strikes)")
                elif(self.solveChoice == "maximize spares"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) maximize(nb_spares)")
                elif(self.solveChoice == "minimize spares"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) minimize(nb_spares)")
                elif(self.solveChoice == "maximize fails"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) maximize(nb_fails)")
                elif(self.solveChoice == "minimize fails"):
                    model.add_string(
                        "\n solve::int_search(partie, dom_w_deg, indomain_max,complete) minimize(nb_fails)")
                # Find the MiniZinc solver configuration for Gecode
                gecode = Solver.lookup("gecode")
                # Create an Instance of the model for Gecode
                instance = Instance(gecode, model)
                # Assign values
                instance["score_total"] = int(score)
                instance["init"] = partie
                # Solve and print solution

                if(self.solveChoice == "satisfy"):
                    self.results = instance.solve(
                        nr_solutions=self.max_sol_number, timeout=timedelta(seconds=2))
                    result = self.results.solution[self.sol_number]
                else:
                    self.results = instance.solve(timeout=timedelta(seconds=2))
                    result = self.results.solution
                nb_fails = result.nb_fails
                nb_spares = result.nb_spares
                nb_strikes = result.nb_strikes

                label_solution = "Solution générée : (" + str(
                    self.sol_number + 1) + "/" + str(len(self.results)) + ")"
                solution = "Lancers : " + convert_to_string(result.partie) + "\n\nNombre de fails : " + str(
                    nb_fails) + "\n\nNombre de spares : " + str(nb_spares) + "\n\nNombre de strikes : " + str(nb_strikes)
            else:
                label_solution = "Erreur :"
                solution = text_erreur

            if self.current_screen.name == "score_window":
                self.ids.view_score_solution_generee.text = solution
                self.ids.view_score_label_solution_generee.opacity = 1
                self.ids.view_score_label_solution_generee.text = label_solution
                self.ids.view_score_solution_generee.opacity = 1
                if len(self.results) <= 1:
                    self.ids.view_score_button_autre_solution.disabled = True
                else:
                    self.ids.view_score_button_autre_solution.disabled = False
            else:
                self.ids.view_complete_solution_generee.text = solution
                self.ids.view_complete_label_solution_generee.opacity = 1
                self.ids.view_complete_label_solution_generee.text = label_solution
                self.ids.view_complete_solution_generee.opacity = 1
                if len(self.results) <= 1:
                    self.ids.view_complete_button_autre_solution.disabled = True
                else:
                    self.ids.view_complete_button_autre_solution.disabled = False

        except ValueError:
            pass

    def AutreSolution(self, button):
        if len(self.results) <= 0:
            return

        if(self.sol_number >= len(self.results) - 1):
            self.sol_number = 0
        else:
            self.sol_number += 1

        result = self.results.solution[self.sol_number]

        nb_fails = result.nb_fails
        nb_spares = result.nb_spares
        nb_strikes = result.nb_strikes

        solution = "Lancers : " + convert_to_string(result.partie) + "\n\nNombre de fails : " + str(
            nb_fails) + "\n\nNombre de spares : " + str(nb_spares) + "\n\nNombre de strikes : " + str(nb_strikes)

        if self.current_screen.name == "score_window":
            self.ids.view_score_solution_generee.text = solution
            self.ids.view_score_label_solution_generee.opacity = 1
            self.ids.view_score_label_solution_generee.text = "Solution générée : (" + str(
                self.sol_number + 1) + "/" + str(len(self.results)) + ")"
            self.ids.view_score_solution_generee.opacity = 1
        else:
            self.ids.view_complete_solution_generee.text = solution
            self.ids.view_complete_label_solution_generee.opacity = 1
            self.ids.view_complete_label_solution_generee.text = "Solution générée : (" + str(
                self.sol_number + 1) + "/" + str(len(self.results)) + ")"
            self.ids.view_complete_solution_generee.opacity = 1

    # def changeSolve(self,button):

#Config.set('graphics', 'width', '1414')
#Config.set('graphics', 'height', '1080')

#kv = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        root = WindowManager()
        root.build()
        return root
        # return kv


MainApp().run()
