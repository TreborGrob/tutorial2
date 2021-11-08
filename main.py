from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
	def build(self):
		return Button(text='Нажми же меня!')
MyApp().run()
