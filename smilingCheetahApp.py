"""
Smilling Cheetah App - Saudação personalizável
    Autor: Júlia Onora da Silva
    Data: 8 de fevereiro de 2022
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SmilingCheetahApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #add widgets to window

        self.window.add_widget(Image(source="smiling_cheetah.jpg"))
        self.greeting = Label(
                        text="Qual é o seu nome?",
                        font_size=38,
                        color="#FF4500"
                        )
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline=False,
                    padding_y=(20, 20),
                    size_hint=(1, 0.5)
                    )

        self.window.add_widget(self.user)

        self.button = Button(
                      text="OK",
                      size_hint=(1, 0.5),
                      bold=True,
                      background_color="#FF4500",
                      background_normal=""
                      )

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Olá " + self.user.text + "!"


if __name__ == "__main__":
    SmilingCheetahApp().run()
