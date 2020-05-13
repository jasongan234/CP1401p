from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_IN_KM = 1.60934


class ConvertMiles(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change=0):
        value = self.get_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def get_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculation(self):
        value = self.get_miles()
        result = value * MILES_IN_KM
        self.root.ids.output_label.text = str(result)


ConvertMiles().run()




