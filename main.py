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

class FinalScr(Screen):
    def __init__(self, name='final'):
        super().__init__(name=name) 
        self.win_label = Label(text="")
        btn = Button(text="перезапустить")
        btn.on_press = self.next

        vertical_layout = BoxLayout(orientation="vertical")
        vertical_layout.add_widget(self.win_label)
        vertical_layout.add_widget(btn)
        self.add_widget(vertical_layout) 

    def next(self):
        self.manager.transition.direction = 'right' 
        #очистить игровой экран
        self.manager.current = 'game'

class Square:
    def __init__(self,*lines):
        self.value = None
        self.button = Button() #потом попробуем покрасить
        self.button.on_press = self.click

        self.lines = lines
        for line in lines:
            line.append(self)
    
    def click(self):
        global player

        if self.value is None: #проставить значение если пустая клетка
            self.value = player
            self.button.text = player
            self.win_check()

            if player == "X":
                player = "O"
            else: 
                player = "X"
      
    def win_check(self):
        for line in self.lines:
            n = 0
            for square in line:
                if square.value == player:
                    n += 1

            if n == 3:
                global sm, final_scr
                final_scr.win_label.text = "победил " + player
                sm.current = "final" #перекидываем на экран финиша (его пока нет)

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
        
        #верхняя
        Square(up,left,diagonal1)
        Square(up,vertical_mid)
        Square(up,right,diagonal2)

        #средний
        Square(mid,left)
        Square(mid,vertical_mid,diagonal1,diagonal2)
        Square(mid,right)

        #нижний
        Square(down,left,diagonal2)
        Square(down,vertical_mid)
        Square(down,right,diagonal1)

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
        global sm, final_scr

        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(GameScr())
        final_scr = FinalScr()
        sm.add_widget(final_scr)
        return sm

player = "X"
app = MyApp()
app.run()
