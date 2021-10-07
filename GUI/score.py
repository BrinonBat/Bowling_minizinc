from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from kivy.graphics import Rectangle


class ScoreWindow(Screen):
    def build(self):

        screen = Screen(name="score_window")

        #BOUTON RETOUR
        button_retour = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Retour", pos_hint={"center_x": .1, "center_y": .9}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_retour.bind(on_release=self.load_menu_window)
        screen.add_widget(button_retour)

        #TITRE
        label_titre = Label(font_size="40px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Générer une partie à partir d'un score", pos_hint={"center_x": .5, "center_y": .8})
        screen.add_widget(label_titre)

        #LABEL SCORE
        label_score = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Score : ", pos_hint={"center_x": .2, "center_y": .6})
        screen.add_widget(label_score)

        #SAISIE SCORE
        score_input = TextInput(size_hint=[None, None], height="40px", width="100px", pos_hint={
                                "center_x": .3, "center_y": .6}, multiline=False)
        # score_input.bind(on_text_validate=self.complete)
        screen.add_widget(score_input)
        self.ids['view_score_input_score'] = score_input

        #BOUTON VALIDER
        button_valider = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Valider", pos_hint={"center_x": .5, "center_y": .6}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_valider.bind(on_press=self.complete)
        screen.add_widget(button_valider)

        #AUTRE SOLUTION
        button_autre_solution = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Autre Solution", pos_hint={"center_x": .8, "center_y": .6}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_autre_solution.bind(on_press=self.AutreSolution)
        screen.add_widget(button_autre_solution)

        #LABEL SOLUTION
        label_solution_generee = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                                       text="Solution générée : ", pos_hint={"center_x": .2, "center_y": .5}, opacity=0)
        screen.add_widget(label_solution_generee)
        self.ids['view_score_label_solution_generee'] = label_solution_generee

        #SOLUTION
        solution_generee = Label(font_size="20px",
                                 pos_hint={"center_x": .3, "center_y": .4}, opacity=0)
        screen.add_widget(solution_generee)
        self.ids['view_score_solution_generee'] = solution_generee

        return screen
