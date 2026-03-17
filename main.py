from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import random

class TicTacToe(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.mode = None
        self.turn = "X"
        self.buttons = []

        self.click_sound = SoundLoader.load("click1.wav")
        self.win_sound = SoundLoader.load("win.wav")
        self.lose_sound = SoundLoader.load("lose.wav")
        self.draw_sound = SoundLoader.load("draw.wav")
        self.bg_music = SoundLoader.load("background.wav")

        if self.bg_music:
            self.bg_music.loop = True
            self.bg_music.play()

        self.status = Label(text="Select Game Mode", font_size=35, size_hint=(1,.2))
        self.add_widget(self.status)

        mode_layout = GridLayout(cols=2, size_hint=(1,.2))

        pvp = Button(text="Player vs Player", background_color=(0.2,0.6,1,1), font_size=22)
        pvc = Button(text="Player vs Computer", background_color=(0.2,1,0.5,1), font_size=22)

        pvp.bind(on_press=self.set_pvp)
        pvc.bind(on_press=self.set_pvc)

        mode_layout.add_widget(pvp)
        mode_layout.add_widget(pvc)

        self.add_widget(mode_layout)

        self.grid = GridLayout(cols=3, spacing=10, padding=20)

        for i in range(9):

            btn = Button(
                text="",
                font_size=60,
                background_color=(0.15,0.15,0.15,1)
            )

            btn.bind(on_press=self.play)
            self.buttons.append(btn)
            self.grid.add_widget(btn)

        self.add_widget(self.grid)

        restart = Button(
            text="Restart Game",
            size_hint=(1,.2),
            font_size=25,
            background_color=(1,0.3,0.3,1)
        )

        restart.bind(on_press=self.restart)
        self.add_widget(restart)

    def set_pvp(self, instance):
        self.mode = "pvp"
        self.status.text = "Player X Turn"

    def set_pvc(self, instance):
        self.mode = "pvc"
        self.status.text = "Your Turn (X)"

    def play(self, instance):

        if self.mode is None:
            self.status.text = "Choose Game Mode!"
            return

        if instance.text == "":

            if self.click_sound:
                self.click_sound.play()

            instance.text = self.turn

            if self.turn == "X":
                instance.color = (0,1,1,1)
            else:
                instance.color = (1,0.5,0,1)

            if self.check_winner():

                if self.mode == "pvc" and self.turn == "O":
                    self.status.text = "Computer Wins!"
                    if self.lose_sound:
                        self.lose_sound.play()
                else:
                    self.status.text = f"Player {self.turn} Wins!"
                    if self.win_sound:
                        self.win_sound.play()

                return

            if self.check_draw():
                self.status.text = "Draw!"
                if self.draw_sound:
                    self.draw_sound.play()
                return

            self.turn = "O" if self.turn == "X" else "X"

            if self.mode == "pvc" and self.turn == "O":
                self.status.text = "Computer Thinking..."
                self.computer_move()
            else:
                self.status.text = f"Player {self.turn} Turn"

    def computer_move(self):

        empty = [btn for btn in self.buttons if btn.text == ""]

        if empty:
            move = random.choice(empty)
            move.text = "O"
            move.color = (1,0.5,0,1)

        if self.check_winner():
            self.status.text = "Computer Wins!"
            if self.lose_sound:
                self.lose_sound.play()
            return

        if self.check_draw():
            self.status.text = "Draw!"
            if self.draw_sound:
                self.draw_sound.play()
            return

        self.turn = "X"
        self.status.text = "Your Turn (X)"

    def check_draw(self):
        return all(btn.text != "" for btn in self.buttons)

    def check_winner(self):

        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for a,b,c in wins:
            if self.buttons[a].text == self.buttons[b].text == self.buttons[c].text != "":
                return True

        return False

    def restart(self, instance):

        for btn in self.buttons:
            btn.text = ""

        self.turn = "X"

        if self.mode == "pvp":
            self.status.text = "Player X Turn"
        elif self.mode == "pvc":
            self.status.text = "Your Turn (X)"
        else:
            self.status.text = "Select Game Mode"

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()


TicTacToeApp().run()

