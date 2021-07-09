from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

KV = '''
MDScreen:
    MDFloatLayout:
        MDIconButton:
            icon: "android"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.show_toast()
            user_font_size: "64sp"
'''

class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def show_toast(self):
        toast('Test Kivy Toast')

Example().run()
print("Test")
print("Test2")
