from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from src.domain.snake_game import SnakeGame

Window.size = (320, 280)


class NewUserGreeting(GridLayout):
    def __init__(self, quit_callback, **kwargs):
        super(NewUserGreeting, self).__init__(**kwargs)
        from src.domain.models.user import GameUser
        self.quit_callback = quit_callback
        self._user = GameUser(name="Bob")
        self.cols = 1
        self.size_hint = (0.7, 0.8)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.add_widget(Image(source="images/snake.png"))
        self.label = Label(
            text="Name: ",
            font_size=40,
            color="#00FFCE",
        )

        self.name_input = TextInput(
            multiline=False,
            font_size=40,
            padding=[10, 10, 10, 10],
            size_hint=(1, 0.5)
        )
        self.name_input.bind(on_text_validate=self.on_name_enter)
        self.add_widget(self.name_input)

        self.add_widget(self.label)
        self.start_button = Button(
            text="Start",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE",
            background_normal="",
        )
        self.start_button.bind(on_press=self.close_window)
        self.add_widget(self.start_button)

    def on_name_enter(self, inp):
        print(inp.text)
        self.label.text = f"Name: {inp.text}"
        self._user.set_name(inp.text)
        self.quit_callback()

    def close_window(self, inp):
        self._user.set_name(self.name_input.text)
        print("USER NAME FORM INPUT ", self._user.get_name())
        self.quit_callback()

    def get_user(self):
        return self._user


class SnakeApp(App):
    def __init__(self):
        super(SnakeApp, self).__init__()
        self.window = None
        self.open_new_user_window()
        self.user = None
        self.user_name = None

    def build(self):
        return self.window

    def open_new_user_window(self):
        self.window = NewUserGreeting(self.quit)

    def quit(self, *args):
        print("Game started!")
        self.user = self.window.get_user()
        self.stop()
        SnakeGame(self.user).start()

    def set_user_name(self, name):
        self.user_name = name


app = SnakeApp()


def main():
    app.run()


if __name__ == "__main__":
    main()
