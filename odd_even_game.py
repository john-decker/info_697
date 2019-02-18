# simple game to help children identify odd or even numbers
# game will begin with instructions 
# game will generate a random number
# game will allow user to use a or b button to make choice
# game will assess the choice and give feed back with a happy or sad face
# game will score the effort and provide that information at the end of the game
# game has animation for various levels of success
# user will be able to play game as many times as s/he would like

from microbit import *
import random

# function generate pseudo-random number between 1 and 50
def get_number_to_fifty():
    number = random.randint(1, 50)
    return number

# function determine whether or not a number is even
def is_even(number):
    if number == 1:
        return False
    elif number % 2 == 0:
        return True
    else:
        return False

# bank of animations to be used for feedback
animation1 = [Image.HEART, Image.HEART_SMALL, Image.HEART, Image.HEART_SMALL,
              Image.HEART, Image.HEART_SMALL]
animation2 = [Image.DIAMOND, Image.DIAMOND_SMALL, Image.DIAMOND,
              Image.DIAMOND_SMALL, Image.DIAMOND, Image.DIAMOND_SMALL]
animation3 = [Image.SQUARE, Image.SQUARE_SMALL, Image.SQUARE,
              Image.SQUARE_SMALL, Image.SQUARE, Image.SQUARE_SMALL]
animation4 = [Image.ARROW_N, Image.ARROW_E, Image.ARROW_S, Image.ARROW_W]

# function to display score message
def score_of_ten_message(score):
    display.scroll("You scored a ")
    sleep(1000)
    display.scroll(score)
    sleep(1000)
    if score == 10:
        display.scroll("PERFECT SCORE!!!")
        display.show(animation1, delay=200)
    elif score > 8:
        display.scroll("Great Job!!!")
        display.show(animation2, delay=200)
    elif score > 6:
        display.scroll("Keep up the Good Work!")
        display.show(animation3, delay=200)
    elif score > 4:
        display.scroll("Keep Practicing!")
        display.show(animation4, delay=200)
    else:
        display.scroll("You can do it!")
        display.show(Image.HAPPY, delay=400)

# begin game
while True:
    score = 0
    display.scroll("Odd or Even Game")
    display.scroll("Press A to Start")

    # initial instructions
    if button_a.was_pressed():
        sleep(1000)
        display.scroll("Let's Go!")
        display.scroll(" ", delay=200)
        display.scroll("Press A for Odd, B for Even")

        # get number and display to user, generates 10 events
        for turn in range(1, 11):
            game_number = get_number_to_fifty()
            display.scroll("..")
            display.scroll(game_number, delay=200)
            display.scroll("..")

            # test answer
            if button_a.was_pressed():
                sleep(1000)
                if is_even(game_number) == True:
                    display.show(Image.SAD)
                    sleep(1000)
                else:
                    display.show(Image.HAPPY)
                    score += 1
                    sleep(1000)
            elif button_b.was_pressed():
                sleep(1000)
                if is_even(game_number) == True:
                    display.show(Image.HAPPY)
                    score += 1
                    sleep(1000)
                else:
                    display.show(Image.SAD)
                    sleep(1000)

        # display score and provide final message
        score_of_ten_message(score)

        # clear for next round of play
        display.clear()
        sleep(2000)

