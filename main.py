# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.uix.label import Label

class MyFirstProgramApp(App):
    def build(self):
        return Label(text = "Hello world!")

if __name__ == "__main__":
    MyFirstProgramApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
