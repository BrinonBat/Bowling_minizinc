from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown


class CompleteWindow(Screen):
    def build(self):
        screen = Screen(name="complete_window")
        # BOUTON RETOUR
        button_retour = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Retour", pos_hint={"center_x": .1, "center_y": .9}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_retour.bind(on_release=self.load_menu_window)
        screen.add_widget(button_retour)

        # TITRE
        label_titre = Label(font_size="40px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Compléter une partie", pos_hint={"center_x": .5, "center_y": .8})
        screen.add_widget(label_titre)

        # LABEL SCORE
        label_score = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="Score : ", pos_hint={"center_x": .2, "center_y": .65})
        screen.add_widget(label_score)

        # INPUT SCORE
        score_input = TextInput(size_hint=[None, None], height="40px", width="100px", pos_hint={
                                "center_x": .3, "center_y": .65}, multiline=False,text="0")
        # score_input.bind(on_text_validate=self.complete)
        screen.add_widget(score_input)
        self.ids['view_complete_input_score'] = score_input

        # LABEL RESOLUTION
        label_resolution = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                                 text="Résolution : ", pos_hint={"center_x": .55, "center_y": .65})
        screen.add_widget(label_resolution)

        # CHOIX SOLVE
        dropdown = DropDown()

        # Boutons minimize spare, maximize spare, minimize fails, maximize fails, minimize strikes, maximize strikes
        btn = Button(text='satisfy', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text),)
        dropdown.add_widget(btn)
        btn = Button(text='maximize strikes', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn = Button(text='minimize strikes', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn = Button(text='maximize spares', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn = Button(text='minimize spares', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn = Button(text='maximize fails', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn = Button(text='minimize fails', size_hint_y=None, height=44, font_size="20px",
                     font_name="fonts/sackers-gothic-std.otf", background_normal='', background_color={1, .3, .4, .85})
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)

        # mise en place du dropdown
        choix_solve = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="satisfy", pos_hint={
                             "center_x": .75, "center_y": .65}, size_hint=[.2, .07], background_normal='', background_color={1, .3, .4, .85})
        choix_solve.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance,
                      x: setattr(choix_solve, 'text', x))
        self.ids['complete_button_choice_solve'] = choix_solve
        screen.add_widget(choix_solve)

        # LABEL SAISIE PARTIE
        label_partie = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                             text="Partie incomplète : ", pos_hint={"center_x": .2, "center_y": .55})
        screen.add_widget(label_partie)

#        partie_input = TextInput(size_hint=[None, None], height="40px", width="500px", pos_hint={
#            "center_x": .2, "center_y": .4}, multiline=False)

        # SAISIE PARTIE
        self.liste_saisie_partie = []
        for i in range(0, 21):
            self.liste_saisie_partie.append(TextInput(size_hint=[None, None], height="30px", width="30px", pos_hint={
                                            "center_x": (i/33.0)+0.35, "center_y": .55}, multiline=False))
            screen.add_widget(self.liste_saisie_partie[i])
            #self.ids['D'+str(i)] = self.liste_saisie_partie[i]
        self.ids['view_complete_input_partie'] = self.liste_saisie_partie

        # BOUTON VALIDER
        button_valider = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Valider", pos_hint={"center_x": .2, "center_y": .45}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_valider.bind(on_press=self.complete)
        screen.add_widget(button_valider)

        # AUTRE SOLUTION
        button_autre_solution = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Autre Solution", pos_hint={"center_x": .4, "center_y": .45}, size_hint=[
            .2, .07], background_normal='', background_color={1, .3, .4, .85})
        button_autre_solution.bind(on_press=self.AutreSolution)
        screen.add_widget(button_autre_solution)
        self.ids['view_complete_button_autre_solution'] = button_autre_solution

        # LABEL SOLUTION
        label_solution_generee = Label(font_size="30px", font_name="fonts/sackers-gothic-std-heavy.otf",
                                       text="Solution générée : ", pos_hint={"center_x": .3, "center_y": .35}, opacity=0)
        screen.add_widget(label_solution_generee)
        self.ids['view_complete_label_solution_generee'] = label_solution_generee

        # SOLUTION
        solution_generee = Label(font_size="25px",
                                 pos_hint={"center_x": .4, "center_y": .2}, opacity=0)
        screen.add_widget(solution_generee)
        self.ids['view_complete_solution_generee'] = solution_generee

        return screen
