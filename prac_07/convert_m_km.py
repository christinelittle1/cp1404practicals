from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometresApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_increment(self, increment, value):
        result = increment + value
        self.root.ids.input_number.text = str(result)

    def convert_miles_to_km(self, miles):
        km = miles * 1.609
        self.root.ids.output_number.text = str(km)


ConvertMilesToKilometresApp().run()
