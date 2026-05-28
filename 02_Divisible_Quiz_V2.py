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

        # Create frames
        # Create a frame to hold all the buttons on the start game gui
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Creates a frame to hold the entry and the play button next to each other within the start_frame
        self.play_button_frame = Frame(self.start_frame)
        self.play_button_frame.grid(row=2, padx=10, pady=10)

        # Reference list to make the buttons for the start game Gui
        # Format [frame, text, width, row, column, command]
        start_buttons_ref = [
            [self.play_button_frame, "Play Game", 15, 0, 1, self.get_rounds],
            [self.start_frame, "Unlimited Mode", 39, 3 ,0, lambda: self.to_game("y")],
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

        # Sends user to the game gui and sends how many rounds they want to play
        PlayGame(num_rounds)

        # Remove box for number of games select
        root.withdraw()


class PlayGame:

    def __init__(self, rounds):
        """ create the GUI for the game and set up all the buttons and variables """

        # Initialize 'self.' variables

        # Setup dialogue box
        self.play_box = Toplevel()

        # Create all the frames
        # Creates a frame to hold the all the button in the play game GUI
        self.play_frame = Frame(self.play_box, padx=10, pady=10)
        self.play_frame.grid()

        # Create a frame to hold the true and false buttons next to each other
        self.true_false_frame = Frame(self.play_frame)
        self.true_false_frame.grid(row=2)

        # Create frame to hold the navigation buttons
        self.nav_frame = Frame(self.play_frame)
        self.nav_frame.grid(row=5)

        # Reference list to make the labels for the start game Gui
        # Format [text, font, row]
        play_labels_ref = [
            ["Question # of #\n# Questions left", "Arial 24 bold", 0],
            ["# Can be divided by #", "Arial 16", 1],
            ["Results will show here", "Arial 16", 3],
            ["Current score: # / #", "Arial 16", 4]
        ]

        # Make list to hold all the start labels after being made to be named after
        self.play_labels = []

        for label in play_labels_ref:
            self.made_label = Label(self.play_frame, text=label[0], font=label[1])
            self.made_label.grid(row=label[2])

            self.play_labels.append(self.made_label)

        # Reference list to make the buttons for the start game Gui
        # Format [frame, text, width, background, command, row, column]
        play_buttons_ref = [
            [self.true_false_frame, "True", 20, "#54fd81", lambda: self.to_ans_check("t"), 0, 0,],
            [self.true_false_frame, "False", 20, "#fd7958", lambda: self.to_ans_check("f"), 0, 1,],
            [self.nav_frame, "Hints", 20, "#229afd", self.to_hints, 0, 0],
            [self.nav_frame, "Next ==>", 20, "#229afd", self.next_round, 0, 1],
            [self.nav_frame, "Stats", 20, "#229afd", self.to_stats, 1, 0],
            [self.nav_frame, "Quit this quiz", 20, "#229afd", self.quit_game(), 1, 1]
        ]

        # Make list to hold all the start buttons after being made to be named after
        self.play_buttons = []

        for button in play_buttons_ref:
            self.made_button = Button(button[0], text=button[1], font="Arial 16", width=button[2], bg=button[3],
                                      command=button[4])
            self.made_button.grid(row=button[5], column=button[6], padx=5, pady=5)

            self.play_buttons.append(self.made_button)

    def to_ans_check(self, response):
        if response == "t":
            print("u have pressed true")
        else:
            print("u have pressed false")


    def to_hints(self):
        print("you are in to hints")


    def to_stats(self):
        print("you are in to stats")


    def next_round(self):
        print("you are in next round")


    def quit_game(self):
        print("you are in quit game")


# Create global variable to hold if the game is currently in infinite mode
unlimited = ""

if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
