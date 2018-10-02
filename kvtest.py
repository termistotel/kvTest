import kivy

kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors.codenavigation import CodeNavigationBehavior
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.lang.parser import ParserException

def kompajliraj(inp,outp,error):
	try:
		tmp = Builder.load_string(inp.text)
		if not tmp:
			error.text = "Nema nista napisano"
	except AttributeError:
		tmp = None
		error.text = "Error: Krivi KV kod"
	except ParserException:
		tmp = None
		error.text = "Error: ParserException"

	outp.clear_widgets()
	if tmp:
		outp.add_widget(tmp)
		error.text = "Nema greske"

class ErrorOut(Label):
	pass

class ReloadButton(Button):
	def on_press(self):
		kompajliraj(self.textRead,self.textWrite,self.errorWrite)

class KVinputText(CodeNavigationBehavior,TextInput):
	pass

class KVoutput(BoxLayout):
	pass

class MainBox(BoxLayout):
  pass


class KvtestApp(App):

		def build(self):
			mainbox = MainBox(orientation="vertical")
			return mainbox

if __name__ == '__main__':
    KvtestApp().run()
