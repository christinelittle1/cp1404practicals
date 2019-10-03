from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.609


class ConvertMilesToKilometresApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    @staticmethod
    def handle_invalid_input(text):
        try:
            miles = float(text)
            return miles
        except ValueError:
            return 0.0

    def handle_increment(self, increment, text):
        result = increment + self.handle_invalid_input(text)
        self.root.ids.input_number.text = str(result)

    def convert_miles_to_km(self, text):
        miles = self.handle_invalid_input(text)
        km = miles * MILES_TO_KM
        self.root.ids.output_number.text = str(km)


ConvertMilesToKilometresApp().run()
