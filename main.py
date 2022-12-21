from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Recordingdoctor(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


Recordingdoctor().run()