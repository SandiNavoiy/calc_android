from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        #Задаем операторы
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        #лейаут верхнего уровня  + виджет верхнего уровня(только для чтения)
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        # добавляем виджет
        main_layout.add_widget(self.solution)
        #список кнопок
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        # Обход по списку кнопок
        for row in buttons:
            #BoxLayout  с горизонтальной ориентацией, по умолчанию
            h_layout = BoxLayout()
            # разложение вложенног списка по кнопкам
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            # Добавляем в основной виджет
            main_layout.add_widget(h_layout)

        # создание и привязка кнопки =
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        ####

        return main_layout

    #метод действий
    def on_button_press(self, instance):
        """Обработчик событий"""
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Проверка наличия двух операторв рядом. не допустимо!
                return
            elif current == "" and button_text in self.operators:
                # Первый символ не может быть оператором
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        """метод выполнения"""
        # выполняется на основе встоеной фунции eval, которая
        # анализирует тестовое выражение и выполняет его
        # есть опасность ввода вредоносного кода
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()

#https://python-scripts.com/kivy-android-ios-exe?ysclid=ls6tc73da2573208528