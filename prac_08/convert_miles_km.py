from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKM(App):
    kilometres = StringProperty()

    def build(self):
        self.title = "Converts Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.kilometres = '54.717'
        return self.root

    def handle_calculate(self):
        miles = self.get_validated_miles()
        kilometres = miles * MILES_TO_KM
        self.kilometres = str(kilometres)

    def handle_increment(self, change):
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


ConvertMilesKM().run()
