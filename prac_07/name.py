from kivy.app import App
from kivy.core.text import Label
from kivy.lang import Builder
from kivy.properties import StringProperty

NAMES = ["Christine", "Bob", "Harry"]


class NameApp(App):
    name_label = StringProperty

    def build(self):
        self.title = "List of Names"
        self.root = Builder.load_file('name.kv')
        return self.root

    def create_labels(self):
        for name in NAMES:
            name_label = Label(text=name)
            name_label.bind()
            self.root.ids.names_box.add_widget(name_label)


NameApp().run()
