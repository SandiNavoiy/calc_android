from kivy.app import App
from kivy.uix.label import Label

#Каждому приложению Kivy требуется
# создать подкласс App и переопределить метод build()
class MainApp(App):
    def build(self):
        label = Label(text='Привет от  Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
#size_hint - размер в процентах от 0 до 1(ширина, высота)
#pos_hint, используется для позиционирования виджета
        return label


if __name__ == '__main__':
    app = MainApp()
    app.run()