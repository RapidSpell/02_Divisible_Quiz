from tkinter import *


# Classes start here
class StartGame:
    """
    Creates first box for the game
    """

    def __init__(self):
        """
        Initialise Divisible quiz
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.title_label = Label(self.start_frame, text="Divisible Quiz",
                                 font="Arial 25 bold")
        self.title_label.grid()

        self.rounds_label = Label(self.start_frame, text="How many rounds do you want to play?",
                          font="Arial 14")
        self.rounds_label.grid(row=1)

        self.play_button_frame = Frame(self.start_frame)
        self.play_button_frame.grid(row=2, padx=10, pady=10)

        self.rounds_input = Entry(self.play_button_frame, font="Arial 19", width=20)
        self.rounds_input.grid(row=0)

        self.play_game_button = Button(self.play_button_frame, text="Play Game", font="Arial 16",
                                       width=15, bg="#229afd")
        self.play_game_button.grid(row=0, column=1)

        self.unlimited_button = Button(self.start_frame, text="Unlimited Mode", font="Arial 16",
                                       width=39, bg="#229afd")
        self.unlimited_button.grid(row=3)


if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
