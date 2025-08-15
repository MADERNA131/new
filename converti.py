from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
'''


class Example(MDApp):
    def on_start(self):
        width = Window.width
        height = Window.height
        print(f"Taille écran détectée : {width} x {height}")
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)


Example().run()