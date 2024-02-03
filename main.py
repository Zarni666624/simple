from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Interface(BoxLayout):
    def add(self):
        # try:
        self.ids.label.text = str(int(str(self.ids.textInput.text)) + int(str(self.ids.textinput.text)))
        '''
        except:
            self.ids.label.text = "Error"
        '''


class SimpleApp(App):
    pass


SimpleApp().run()
