
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


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
            temp_button = Label(text=names, id=names)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicLabels().run()



