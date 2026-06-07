from tkinter import *
import random


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
        self.total_rounds = rounds

        # Variable to hold how many rounds have been played
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # variable to save how many correct answers the user has put
        self.ans_correct = 0

        # variable to hold if the current question it true of false
        self.true_false = int

        # variable to hold the divisor and dividend
        self.divisor = int
        self.dividend = int
        self.result = int

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

        # name the labels so they can be configured later
        self.question_num_label = self.play_labels[0]
        self.question_label = self.play_labels[1]
        self.result_label = self.play_labels[2]
        self.score_label = self.play_labels[3]


        # Reference list to make the buttons for the start game Gui
        # Format [frame, text, width, background, command, row, column]
        play_buttons_ref = [
            [self.true_false_frame, "True", 20, "#54fd81", lambda: self.to_ans_check("t"), 0, 0,],
            [self.true_false_frame, "False", 20, "#fd7958", lambda: self.to_ans_check("f"), 0, 1,],
            [self.nav_frame, "Hints", 20, "#229afd", self.to_hints, 0, 0],
            [self.nav_frame, "Next Question ==>", 20, "#229afd", self.new_round, 0, 1],
            [self.nav_frame, "Stats", 20, "#229afd", self.to_stats, 1, 0],
            [self.nav_frame, "Quit this quiz", 20, "#229afd", self.quit_game, 1, 1]
        ]

        # Make list to hold all the start buttons after being made to be named after
        self.play_buttons = []

        for button in play_buttons_ref:
            self.made_button = Button(button[0], text=button[1], font="Arial 16", width=button[2], bg=button[3],
                                      command=button[4])
            self.made_button.grid(row=button[5], column=button[6], padx=5, pady=5)

            self.play_buttons.append(self.made_button)

        # Name the buttons so they can be configured later
        self.true_button = self.play_buttons[0]
        self.false_button = self.play_buttons[1]

        self.next_button = self.play_buttons[3]
        self.stats_button = self.play_buttons[4]

        # send user the user to new_round function to start the game
        self.new_round()


    def new_round(self):
        """ edits the labels to display the correct information and questions"""
        # unable True and False buttons and disable the next button
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)

        # if the user is on their first round disable the stats button
        if self.rounds_played.get() == 0:
            self.stats_button.config(state=DISABLED)

        # if user is no longer on the first round enable the stats button
        else:
            self.stats_button.config(state=NORMAL)

        # add one to rounds played
        self.rounds_played.set(self.rounds_played.get() + 1)

        # setup questions left label if not in unlimited mode
        if unlimited == "n":
            # configure the labels
            self.question_num_label.config(text=f"Question {self.rounds_played.get()} of {self.total_rounds}\n{self.total_rounds - self.rounds_played.get()} Questions left")
        
        else:
            self.question_num_label.config(
                text=f"You are playing infinite mode")


        # decide if it is going to be true of false
        self.true_false = random.randint(0, 1)

        # Choose number to divide by
        self.divisor = random.randint(1, 10)

        # if answer is going to be true (true_false = 0) find a multiple of the divisor
        if self.true_false == 0:
            self.dividend = self.divisor * random.randint(1, 10)

        else:
            while True:
                temp_dividend = random.randint(1,100)

                try:
                    correct = int(temp_dividend / self.divisor)

                    self.dividend = temp_dividend
                    break

                except ValueError:
                    print("failed")

        # configure the question label
        self.question_label.config(text=f"{self.dividend} Can be divided by {self.divisor}")

        self.result = self.dividend / self.divisor
        print(self.result)


    def to_ans_check(self, response):
        """ check if the user pressed the right answer"""

        # when the user has pressed true or false disable true and false buttons
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

        # if the user not on their last round enable the next button  so they can continue to the next question
        if self.total_rounds - self.rounds_played.get() != 0 or unlimited == "y":
            self.next_button.config(state=NORMAL)

        else:
            self.next_button.config(text="This is your last round")

        # If the user pressed true
        if response == "t":
            # If the user was correct
            if self.true_false == 0:
                self.result_label.config(text=f"{self.dividend} CAN be divided by {self.divisor} the answer is {self.result}", bg="#54fd81")
                self.ans_correct += 1

            else:
                self.result_label.config(text=f"{self.dividend} CANT be divided by {self.divisor} the answer is {self.result}", bg="#fd7958")

        # If the user pressed false
        else:
            # If the user was correct
            if self.true_false == 1:
                self.result_label.config(text=f"{self.dividend} CANT be divided by {self.divisor} the answer is {self.result}", bg="#54fd81")
                self.ans_correct += 1

            else:
                self.result_label.config(text=f"{self.dividend} CAN be divided by {self.divisor} the answer is {self.result}", bg="#fd7958")

        # configure the current score label
        self.score_label.config(text=f"current score: {self.ans_correct}/{self.rounds_played.get()}")


    def to_hints(self):
        """ sends user to the Hints class so it displays the hints GUI"""
        Hints(self)


    def to_stats(self):
        print("you are in to stats")


    def quit_game(self):
        """ sends user back to the start GUI """
        # open start gui
        root.deiconify()

        # close game tab
        self.play_box.destroy()


class Hints:
    def __init__(self, partner):
        """ create GUI and labels in the hints page """

        print("success")


# Create global variable to hold if the game is currently in infinite mode
unlimited = ""

if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
