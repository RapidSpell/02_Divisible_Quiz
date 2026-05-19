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

        # create a frame to hold all the buttons on the start game gui
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Creates the title label
        self.title_label = Label(self.start_frame, text="Divisible Quiz",
                                 font="Arial 25 bold")
        self.title_label.grid()

        # Creates question label to make it clear what the users should put in the entry box
        self.rounds_label = Label(self.start_frame, text="How many rounds do you want to play?",
                          font="Arial 14")
        self.rounds_label.grid(row=1)

        # Creates a frame to hold the entry and the play button next to each other within the start_frame
        self.play_button_frame = Frame(self.start_frame)
        self.play_button_frame.grid(row=2, padx=10, pady=10)

        # Creates the entry box to get the number of rounds the user wants to play
        self.rounds_input = Entry(self.play_button_frame, font="Arial 19", width=20)
        self.rounds_input.grid(row=0)

        # Creates play game button to send user to the play game gui
        self.play_game_button = Button(self.play_button_frame, text="Play Game", font="Arial 16",
                                       width=15, bg="#229afd", command=self.get_rounds)
        self.play_game_button.grid(row=0, column=1)

        # Creates unlimited mode button to set the game to unlimited mode and send the user to the
        self.unlimited_button = Button(self.start_frame, text="Unlimited Mode", font="Arial 16",
                                       width=39, bg="#229afd", command=lambda:self.to_game("y"))
        self.unlimited_button.grid(row=3)


    def get_rounds(self):
        """ gets the value from the input box and checks it is valid and set rounds to the correct number """
        print("you r in get rounds")
        num_rounds = 3

        # Sends user to to_game and sets infinite mode to "n" and gives the number of rounds the user wants to play
        self.to_game("n", num_rounds)


    def to_game(self, unlimited_mode, num_rounds=0):
        """ sends user to the PlayGame class """
        # Create global to hold if the game is currently in infinite mode
        global unlimited
        unlimited = unlimited_mode
        print("unlimited mode =", unlimited)
        print("num rounds =", num_rounds)

        PlayGame()


class PlayGame:

    def __init__(self):
        """ create the gui for the game and set up all the buttons and variables """


if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
