from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.uix.button import Button


class MenuWindow(Screen):
    def build(self):
        screen = Screen(name="menu_window")

        label_titre = Label(font_size="60px", font_name="fonts/sackers-gothic-std-heavy.otf",
                            text="B  O  W  L  I  N  G", pos_hint={"center_x": .3, "center_y": .7})
        screen.add_widget(label_titre)

        button_generate = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Générer une partie", pos_hint={"center_x": .3, "center_y": .5}, size_hint=[
                                 .3, .07], background_normal='', background_color={1, .3, .4, .85})
        button_generate.bind(on_release=self.load_score_window)
        screen.add_widget(button_generate)

        button_complete = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Compléter une partie", pos_hint={"center_x": .3, "center_y": .4}, size_hint=[
                                 .3, .07], background_normal='', background_color={1, .3, .4, .85})
        button_complete.bind(on_release=self.load_complete_window)
        screen.add_widget(button_complete)

        button_quit = Button(font_size="25px", font_name="fonts/sackers-gothic-std.otf", text="Quitter", pos_hint={"center_x": .9, "center_y": .1}, size_hint=[
            .15, .07], background_normal='', background_color={1, .3, .4, .85})
        button_quit.bind(on_release=self.quit)
        screen.add_widget(button_quit)

        return screen
