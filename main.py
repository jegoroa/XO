from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) 
        btn = Button(text="начать игру")
        btn.on_press = self.next
        self.add_widget(btn) 

    def next(self):
        self.manager.transition.direction = 'left' 
        self.manager.current = 'game'

class Square:
    def __init__(self):
        self.value = None
        self.button = Button() #потом попробуем покрасить

class GameScr(Screen):
    def __init__(self, name='game'):
        super().__init__(name=name)
        #наполнить кнопками
        up_layout = BoxLayout(orientation="horizontal")
        mid_layout = BoxLayout(orientation="horizontal")
        down_layout = BoxLayout(orientation="horizontal")

        up = []
        mid = []
        down = []
        left = []
        vertical_mid = []
        right = []
        diagonal1 = []
        diagonal2 = []
        
        f = Square()
        up.append(f)
        left.append(f)
        diagonal1.append(f)
            
        f = Square()
        up.append(f)
        vertical_mid.append(f)

        f = Square()
        up.append(f)
        right.append(f)
        diagonal2.append(f)
        #верхнюю закончили

        f = Square()
        down.append(f)
        left.append(f)
        diagonal2.append(f)
            
        f = Square()
        down.append(f)
        vertical_mid.append(f)

        f = Square()
        down.append(f)
        right.append(f)
        diagonal1.append(f)
        #нижний готово

        f = Square()
        mid.append(f)
        left.append(f)
            
        f = Square()
        mid.append(f)
        vertical_mid.append(f)
        diagonal1.append(f)
        diagonal2.append(f)

        f = Square()
        mid.append(f)
        right.append(f)

        for square in up:
            up_layout.add_widget(square.button)
        for square in mid:
            mid_layout.add_widget(square.button)
        for square in down:
            down_layout.add_widget(square.button)
        
        vertical_layout = BoxLayout(orientation="vertical")
        vertical_layout.add_widget(up_layout)
        vertical_layout.add_widget(mid_layout)
        vertical_layout.add_widget(down_layout)
        self.add_widget(vertical_layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(GameScr())
        return sm

app = MyApp()
app.run()
