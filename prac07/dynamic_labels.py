"""https://github.com/jasongan234/CP1401p/blob/master/prac07/dynamic_labels.py"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabels(App):
    def __init__(self):
        super().__init__()
        self.names = ["Jason", "Jessie", "Jackson"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for names in self.names:
            temp_button = Button(text=names, id=names)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicLabels().run()



