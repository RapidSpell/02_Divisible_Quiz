from tkinter import *
from RangeSlider.RangeSlider import RangeSliderH


# Classes start here
class StartGame:
    """
    Creates first box for the game
    """

    def __init__(self):
        """
        Initialise Divisible quiz
        """

        # Create frames
        # Create a frame to hold all the buttons on the start game gui
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Create a frame to hold easy and hard buttons
        self.easy_hard_frame = Frame(self.start_frame)
        self.easy_hard_frame.grid(row=2, padx=10, pady=10)

        # Creates a frame to hold the entry and the play button next to each other within the start_frame
        self.play_button_frame = Frame(self.start_frame)
        self.play_button_frame.grid(row=3)

        # Reference list to make the buttons for the start game Gui
        # Format [frame, text, width, row, column, command]
        start_buttons_ref = [
            [self.easy_hard_frame, "Easy Mode", 15, 0, 0, lambda: self.mode("easy")],
            [],
            [self.play_button_frame, "Play Game", 15, 0, 1, self.get_rounds],
            [self.start_frame, "Unlimited Mode", 39, 4 ,0, lambda: self.to_game("y")],
        ]

        # Make list to hold all the start buttons after being made to be named after
        self.start_buttons = []

        for button in start_buttons_ref:
            self.made_button = Button(button[0], text=button[1], font="Arial 16", width=button[2], bg="#229afd",
                                      command=button[5])
            self.made_button.grid(row=button[3], column=button[4])

            self.start_buttons.append(self.made_button)

        # Reference list to make the labels for the start game Gui
        # Format [text, font, row]
        start_labels_ref = [
            ["Divisible quiz", "Arial 25 bold", 0],
            ["How many rounds do you want to play?", "Arial 14", 1],
        ]

        # Make list to hold all the start labels after being made to be named after
        self.start_labels = []

        for label in start_labels_ref:
            self.made_label = Label(self.start_frame, text=label[0], font=label[1])
            self.made_label.grid(row=label[2])

            self.start_labels.append(self.made_label)

        self.rounds_label = self.start_labels[1]

        # Creates the entry box to get the number of rounds the user wants to play
        self.rounds_input = Entry(self.play_button_frame, font="Arial 19", width=20)
        self.rounds_input.grid(row=0)


    def mode(self, mode_type):
        """ sets the mode and updates the buttons """


    def get_rounds(self):
        """ gets the value from the input box and checks it is valid and set rounds to the correct number """
        try:
            # Checks if the user has entered an integer
            num_rounds = int(self.rounds_input.get())

            if 0 < num_rounds <= 100:
                # Sends user to to_game and sets infinite mode to "n" and gives the number of rounds the user wants to play
                self.to_game("n", num_rounds)
                self.rounds_label.configure(text="How many rounds do you want to play?", fg="#000000")

            else:
                # If the user inputs an invalid integer change the text and text colour of the label to indicate there is an issue
                self.rounds_label.config(text="Please enter an integer between 0 and 100", fg="#fd7958")


        except ValueError:
            # If the user inputs an invalid integer change the text and text colour of the label to indicate there is an issue
            self.rounds_label.config(text="Please enter an integer between 0 and 100", fg="#fd7958")


    def to_game(self, unlimited_mode, num_rounds=0):
        """ sends user to the PlayGame class """
        global unlimited
        unlimited = unlimited_mode

        # create list for easy mode  options
        mode = "hard"

        print(mode)


# Create global variable to hold if the game is currently in infinite mode
unlimited = ""

if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
