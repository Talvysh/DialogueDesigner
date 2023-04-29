from kivy.app import App
from kivy.uix.widget import Widget


class DialogueDesigner(Widget):
    pass


class DDApp(App):
    def build(self):
        return DialogueDesigner()


if __name__ == "main":
    DDApp.run()