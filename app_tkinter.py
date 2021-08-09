# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30


# function that will start the game.
def startGame(event):
    if timeleft == 30:
        # start the countdown timer.
        countdown()

    # run the function to
    # choose the next colour.
    nextColour()


# Function to choose and
# display the next colour.
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))

