from kivy.uix.screenmanager import Screen

"""
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
        
        if result.status==Status.SATISFIED:
            solution.set(result["partie"])
        else :
            solution.set("UNSATISFIABLE")
        

        self.current_screen.solution_generee.text = result["partie"]
        print(result["partie"])
    except ValueError:
        pass

    self.current_screen.label_solution_generee.opacity = 1
    self.current_screen.solution_generee.opacity = 1
"""
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CompleteWindow(Screen):
    def build(self):
        screen = Screen(name="complete_window")
        # BOUTON RETOUR
        button_retour = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Retour", pos_hint={"center_x": .1, "center_y": .9}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_retour.bind(on_release=self.load_menu_window)
        screen.add_widget(button_retour)

        #TITRE
        label_titre = Label(font_size="40px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Compléter une partie", pos_hint={"center_x": .5, "center_y": .8})
        screen.add_widget(label_titre)

        label_score = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Score : ", pos_hint={"center_x": .2, "center_y": .6})
        screen.add_widget(label_score)

        #INPUT SCORE
        score_input = TextInput(size_hint=[None, None], height="40px", width="100px", pos_hint={
                                "center_x": .3, "center_y": .6}, multiline=False)
        # score_input.bind(on_text_validate=self.complete)
        screen.add_widget(score_input)
        self.ids['view_complete_input_score'] = score_input

        #LABEL SAISIE PARTIE
        label_partie = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                             text="Partie incomplète : ", pos_hint={"center_x": .2, "center_y": .5})
        screen.add_widget(label_partie)

#        partie_input = TextInput(size_hint=[None, None], height="40px", width="500px", pos_hint={
#            "center_x": .2, "center_y": .4}, multiline=False)        
        
        #SAISIE PARTIE
        self.liste_saisie_partie=[]
        for i in range(0,21):
            self.liste_saisie_partie.append(TextInput(size_hint=[None, None], height="30px", width="30px", pos_hint={"center_x": (i/21.0)+0.025,"center_y": 0.4}, multiline=False) )
            screen.add_widget(self.liste_saisie_partie[i])
            #self.ids['D'+str(i)] = self.liste_saisie_partie[i]
        self.ids['view_complete_input_partie']=self.liste_saisie_partie

        #BOUTON VALIDER
        button_valider = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Valider", pos_hint={"center_x": .5, "center_y": .3}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_valider.bind(on_press=self.complete)
        screen.add_widget(button_valider)

        #LABEL SOLUTION
        label_solution_generee = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                                       text="Solution générée : ", pos_hint={"center_x": .2, "center_y": .2}, opacity=0)
        screen.add_widget(label_solution_generee)
        self.ids['view_complete_label_solution_generee'] = label_solution_generee

        #SOLUTION
        solution_generee = Label(font_size="20px",
                                 pos_hint={"center_x": .3, "center_y": .1}, opacity=0)
        screen.add_widget(solution_generee)
        self.ids['view_complete_solution_generee'] = solution_generee

        return screen
