from pstats import Stats
from tkinter import *
import random
from functools import partial


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
        self.hints_button = self.play_buttons[2]
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
        if self.true_false == 0:
            self.divisor = random.randint(1, 10)

        # if the question is going to be false divisor cannot be 1 because every whole number is divisible by one
        else:
            self.divisor = random.randint(2, 10)

        # if answer is going to be true (true_false = 0) find a multiple of the divisor
        if self.true_false == 0:
            print("is true")
            self.dividend = self.divisor * random.randint(1, 10)

        else:
            print("is false")

            while True:
                temp_dividend = random.randint(1,100)

                if temp_dividend / self.divisor != int(temp_dividend / self.divisor):

                    self.dividend = temp_dividend
                    break

                else:
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
        """ Sends user to hints GUI and disables hints button """
        # Disable hints button so multiple hint GUI's cannot be created
        self.hints_button.config(state=DISABLED)

        Hints(self)


    def to_stats(self):
        """ sends user to stats GUI and disables the stats button """
        # Disables stats button
        self.stats_button.config(state=DISABLED)

        RoundStats(self)


    def quit_game(self):
        """ sends user back to the start GUI """
        # open start gui
        root.deiconify()

        # close game tab
        self.play_box.destroy()


class Hints:
    def __init__(self, partner):
        """ create GUI and labels in the hints page """

        # Create box to hold hints labels
        self.hints_box = Toplevel(bg="#FFE6CC")

        # if users press cross at the top, coses help and
        # 'releases' help button
        self.hints_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_hints, partner))

        # Create a coloured frame to hold the labels
        self.hints_frame = Frame(self.hints_box, bg="#FFE6CC")
        self.hints_frame.grid(padx=10, pady=10)

        # Create labels for hints
        self.hints_intro_label = Label(self.hints_frame, text="If you are struggling with this quiz you've\ncome to the right place.\n\n"
                                                              "For certain divisions there is rules that you\n"
                                                              "can use to help you, bellow are the rules for\n"
                                                              "divisions up to 10:", bg="#FFE6CC", font="Arial 16")
        self.hints_intro_label.grid(row=0)

        self.rules_label = Label(self.hints_frame, text="""1. every whole number is divisible by 1 (this game will only\ngive you whole numbers)
2. if the last digit is even (0, 2, 4, 6, 8)
3. the sum of the digits is divisible by 3 (126, 1+2+6 = 9,\n9/3 = whole number therefore 126 is divisible by 9)
4. if the last 2 digits are divisible by 4
5. if the last digit is 0 or 5
6. if the number is divisible by 3 and 2
7. there is no simple rules for divisions by 7
8. the last 3 digits of the number are divisible by 8
9. sum of digits is divisible by 9
10. if final digit is 0""", bg="#FFE6CC", font="Arial 12")
        self.rules_label.grid(row=1)

        self.gl_label = Label(self.hints_frame, text="I hope this helps and Good Luck!", bg="#FFE6CC", font="Arial 16")
        self.gl_label.grid(row=2)

        self.return_button = Button(self.hints_frame, text="Return", bg="#229afd", font="Arial 16", padx=20, pady=5,
                                    command=lambda: self.close_hints(partner))
        self.return_button.grid(row=3)


    def close_hints(self, partner):
        """ close the hints GUI """
        self.hints_box.destroy()

        partner.hints_button.config(state=NORMAL)


class RoundStats:
    def __init__(self, partner):
        """ Opens a GUI to show the stats and the export results button """
        # Create a box to hold all the boxes in the stats GUI
        self.stats_box = Toplevel()

        # if users press cross at the top, coses help and
        # 'releases' help button
        self.stats_box.protocol("WM_DELETE_WINDOW",
                                partial(self.close_stats, partner))

        # create frame to hold everything it the stats GUI
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid(padx=10, pady=10)

        # Create title label
        self.stats_title_label = Label(self.stats_frame, text="Stats/Export", font="Arial 20")
        self.stats_title_label.grid(row=0)

        # Create frame to hold all the stats
        self.result_frame = Frame(self.stats_frame, bg="#FFE6CC", padx=10, pady=10)
        self.result_frame.grid(row=1)

        # Create frame to hold answers correct label and win rate label next to each other
        self.result_stats_frame = Frame(self.result_frame, bg="#FFE6CC", padx=10, pady=10)
        self.result_stats_frame.grid(row=0)

        # Create label to show answers correct
        self.ans_correct_label = Label(self.result_stats_frame, text="Answers Correct:\n#/#", font="Arial 16", bg="#FFE6CC")
        self.ans_correct_label.grid(row=0, column=0, padx=10)

        # Create label to show win rate
        self.win_rate_label = Label(self.result_stats_frame, text="Win Rate:\n##%", font="Arial 16", bg="#FFE6CC")
        self.win_rate_label.grid(row=0, column=1, padx=10)

        # Create a Label to show the most recent questions and answers
        self.history_label = Label(self.result_frame, text="History:\n*history is shown here*", font="Arial 16", bg="#FFE6CC")
        self.history_label.grid(row=1, column=0)

        # frame to hold the return and the export button
        self.stats_nav_frame = Frame(self.stats_frame)
        self.stats_nav_frame.grid(row=2)

        # Create button to close stats
        self.stats_return_button = Button(self.stats_nav_frame, text="Return", width=20, bg="#229afd",
                                          command=lambda: self.close_stats(partner), font="Arial 20")
        self.stats_return_button.grid(row=0, column=0)


    def close_stats(self, partner):
        """ closes the stats GUI and enables the stats button """
        self.stats_box.destroy()

        partner.stats_button.config(state=NORMAL)


# Create global variable to hold if the game is currently in infinite mode
unlimited = ""

if __name__ == "__main__":
    root = Tk()
    root.title("Divisible Quiz")
    StartGame()
    root.mainloop()
