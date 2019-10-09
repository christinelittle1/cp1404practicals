from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class NameApp(App):
    name_label = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Christine", "Bob", "Harry"]

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('name.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.names_box.add_widget(name_label)


NameApp().run()
