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

        # reference list to make the buttons for the start game Gui
        # format [name, frame, text, font, width, background, row, column, padding, command]
        start_buttons_ref = [
            [],
            []
        ]

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
                                       width=39, bg="#229afd", command=lambda: self.to_game("y"))
        self.unlimited_button.grid(row=3)

    def get_rounds(self):
        """ gets the value from the input box and checks it is valid and set rounds to the correct number """
        try:
            # checks if the user has entered an integer
            num_rounds = int(self.rounds_input.get())

            if 0 < num_rounds <= 100:
                # Sends user to to_game and sets infinite mode to "n" and gives the number of rounds the user wants to play
                self.to_game("n", num_rounds)
                self.rounds_label.configure(text="How many rounds do you want to play?", fg="#000000")

            else:
                # if the user inputs an invalid integer change the text and text colour of the label to indicate there is an issue
                self.rounds_label.config(text="Please enter an integer between 0 and 100", fg="#fd7958")


        except ValueError:
            # if the user inputs an invalid integer change the text and text colour of the label to indicate there is an issue
            self.rounds_label.config(text="Please enter an integer between 0 and 100", fg="#fd7958")

    def to_game(self, unlimited_mode, num_rounds=0):
        """ sends user to the PlayGame class """
        global unlimited
        unlimited = unlimited_mode

        # sends user to the game gui and sends how many rounds they want to play
        PlayGame(num_rounds)

        # remove box for number of games select
        root.withdraw()


class PlayGame:

    def __init__(self, rounds):
        """ create the GUI for the game and set up all the buttons and variables """

        # initialize 'self.' variables

        # setup dialogue box
        self.play_box = Toplevel()

        # creates a grid to hold the all the button in the play game GUI
        self.play_frame = Frame(self.play_box, padx=10, pady=10)
        self.play_frame.grid()

        # Create question left label
        self.question_num_label = Label(self.play_frame, text="Question # of #\n# Questions left", font="Arial 24 bold")
        self.question_num_label.grid()

        self.question_label = Label(self.play_frame, text="# Can be divided by #", font="Arial 16")
        self.question_label.grid(row=1)

        self.true_false_frame = Frame(self.play_frame)
        self.true_false_frame.grid(row=2)

        self.true_button = Button(self.true_false_frame, text="True", bg="#54fd81", font="Arial 16 bold", height=2,
                                  width=20)
        self.true_button.grid(row=0, column=0, padx=5, pady=5)

        self.false_button = Button(self.true_false_frame, text="False", bg="#fd7958", font="Arial 16 bold", height=2,
                                   width=20)
        self.false_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_label = Label(self.play_frame, text="Results will show here", font="Arial 16")
        self.result_label.grid(row=3)

        self.score_label = Label(self.play_frame, text="Current score: # / #", font="Arial 16")
        self.score_label.grid(row=4)

        self.nav_frame = Frame(self.play_frame)
        self.nav_frame.grid(row=5)

        self.hints_button = Button(self.nav_frame, text="Hints", bg="#229afd", font="Arial 16 bold", height=2, width=20)
        self.hints_button.grid(row=0, column=0, padx=5, pady=5)

        self.next_button = Button(self.nav_frame, text="Next ==>", bg="#229afd", font="Arial 16 bold", height=2,
                                  width=20)
        self.next_button.grid(row=0, column=1, padx=5, pady=5)

        self.stats_button = Button(self.nav_frame, text="Stats", bg="#229afd", font="Arial 16 bold", height=2, width=20)
        self.stats_button.grid(row=1, column=0, padx=5, pady=5)

        self.quit_button = Button(self.nav_frame, text="Quit this quiz", bg="#229afd", font="Arial 16 bold", height=2,
                                  width=20)
        self.quit_button.grid(row=1, column=1, padx=5, pady=5)


# Create global variable to hold if the game is currently in infinite mode
unlimited = ""

if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
