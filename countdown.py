# import everything from tkinter module and random package
from tkinter import *
import random
import time
from pygame import mixer  # Load the popular external library

# globally declare the expression variable
expression = ""

number_last_character = False


# Function to update expression in the text entry box
def press_operator(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

    global number_last_character
    number_last_character = False


# Function to update expression in the text entry box
def press_number(num):

    global number_last_character

    if not number_last_character:
        # point out the global expression variable
        global expression

        # concatenation of string
        expression = expression + str(num)

        # update the expression by using set method
        equation.set(expression)

        number_last_character = True


# Function to clear the contents of text entry box
def clear():
    global expression
    global number_last_character
    expression = ""
    equation.set("")
    number_last_character = False


# ***** Game calculations *****
def start(large_numbers_choice):
    global selected_numbers
    global target
    global number_last_character
    number_last_character = False
    selected_numbers = []

    large_numbers = [25, 50, 75, 100]
    small_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    random.shuffle(large_numbers)
    random.shuffle(small_numbers)
    small_numbers_choice = 6 - large_numbers_choice

    while large_numbers_choice > 0:
        large_number = large_numbers.pop()
        selected_numbers.append(large_number)
        large_numbers_choice -= 1

    while small_numbers_choice > 0:
        small_number = small_numbers.pop()
        selected_numbers.append(small_number)
        small_numbers_choice -= 1

    global number_1
    number_1 = selected_numbers[0]
    button1['text'] = number_1
    time.sleep(1)
    gui.update()

    global number_2
    number_2 = selected_numbers[1]
    button2['text'] = number_2
    time.sleep(1)
    gui.update()

    global number_3
    number_3 = selected_numbers[2]
    button3['text'] = number_3
    time.sleep(1)
    gui.update()

    global number_4
    number_4 = selected_numbers[3]
    button4['text'] = number_4
    time.sleep(1)
    gui.update()

    global number_5
    number_5 = selected_numbers[4]
    button5['text'] = number_5
    time.sleep(1)
    gui.update()

    global number_6
    number_6 = selected_numbers[5]
    button6['text'] = number_6
    time.sleep(1)
    gui.update()

    # Delay for 1 second then loop through random 3-digit target values for 3 seconds
    time.sleep(1)
    i = 120
    while i >= 0:
        target = random.randint(100, 999)
        label_target['text'] = target
        time.sleep(0.025)
        gui.update()
        i -= 1

    # Play the game show music
    mixer.init()
    mixer.music.load('the-countdown-clock.mp3')
    mixer.music.play()


# Function to evaluate the final expression
def equal_press():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression
        global target
        global number_last_character
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = int(eval(expression))

        if total == target:
            submit_message = "\nAmazing!  10 points for the exact solution."
        elif target - 5 <= total <= target + 5:
            submit_message = "\nWell done, you scored 7 points\nfor getting within 5 of the target."
        elif target - 10 <= total <= target + 10:
            submit_message = "\nOkay... you scored 5 points\nfor getting within 10 of the target."
        else:
            submit_message = "\nNot even close."

        equation.set(str(total) + submit_message)

        # initialize the expression variable
        # by empty string
        expression = ""
        number_last_character = False

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light blue")

    # set the title of GUI window
    gui.title("Countdown Numbers Game")

    # set the configuration of GUI window
    gui.geometry("710x500")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Label(gui, textvariable=equation, bg='light blue', font=('Helvetica', 16, 'bold'))

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(row=16, column=1, rowspan=6, columnspan=6)

    equation.set('Use the buttons to enter your solution')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    selected_numbers = []
    number_1 = ''
    number_2 = ''
    number_3 = ''
    number_4 = ''
    number_5 = ''
    number_6 = ''
    target = ''

    label_target = Label(gui, text=target, bg='black', fg='yellow', font=('Helvetica', 36, 'bold'))
    label_target.grid(row=10, column=3, columnspan=3, sticky="nsew", padx=40, pady=10)

    welcome_text = "Welcome to the Countdown Numbers Game!\nPlease select your desired amount of large numbers:"
    label_welcome = Label(gui, text=welcome_text, bg='light blue', font=('Helvetica', 14, 'bold'))
    label_welcome.grid(row=0, column=1, columnspan=8)

    label_space = Label(gui, text='', bg='light blue', font=('Helvetica', 12, 'bold'), width=7)
    label_space.grid(row=0, column=0)

    button1 = Button(gui, text=number_1, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_1), height=1, width=7)
    button1.grid(row=14, column=1)

    button2 = Button(gui, text=number_2, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_2), height=1, width=7)
    button2.grid(row=14, column=2)

    button3 = Button(gui, text=number_3, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_3), height=1, width=7)
    button3.grid(row=14, column=3)

    button4 = Button(gui, text=number_4, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_4), height=1, width=7)
    button4.grid(row=14, column=4)

    button5 = Button(gui, text=number_5, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_5), height=1, width=7)
    button5.grid(row=14, column=5)

    button6 = Button(gui, text=number_6, fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                     command=lambda: press_number(number_6), height=1, width=7)
    button6.grid(row=14, column=6)

    # Buttons: arithmetic operators
    plus = Button(gui, text=' + ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                  command=lambda: press_operator("+"), height=1, width=7)
    plus.grid(row=16, column=8)

    minus = Button(gui, text=' - ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                   command=lambda: press_operator("-"), height=1, width=7)
    minus.grid(row=17, column=8)

    multiply = Button(gui, text=' x ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                      command=lambda: press_operator("*"), height=1, width=7)
    multiply.grid(row=18, column=8)

    divide = Button(gui, text=' / ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                    command=lambda: press_operator("/"), height=1, width=7)
    divide.grid(row=19, column=8)

    open_bracket = Button(gui, text=' ( ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                          command=lambda: press_operator("("), height=1, width=7)
    open_bracket.grid(row=20, column=8)

    close_bracket = Button(gui, text=' ) ', fg='white', bg='blue', font=('Helvetica', 12, 'bold'),
                           command=lambda: press_operator(")"), height=1, width=7)
    close_bracket.grid(row=21, column=8)

    equal = Button(gui, text='Submit', fg='white', bg='green', font=('Helvetica', 12, 'bold'),
                   command=equal_press, height=1, width=7)
    equal.grid(row=22, column=1, columnspan=3, sticky="nsew")

    clear = Button(gui, text='Clear', fg='white', bg='red', font=('Helvetica', 12, 'bold'),
                   command=clear, height=1, width=7)
    clear.grid(row=22, column=4, columnspan=3, sticky="nsew")

    large_0 = Button(gui, text='0', fg='white', bg='grey', font=('Helvetica', 12, 'bold'),
                     command=lambda: start(0), height=1, width=7)
    large_0.grid(row=1, column=2, pady=10)

    large_1 = Button(gui, text='1', fg='white', bg='grey', font=('Helvetica', 12, 'bold'),
                     command=lambda: start(1), height=1, width=7)
    large_1.grid(row=1, column=3, pady=10)

    large_2 = Button(gui, text='2', fg='white', bg='grey', font=('Helvetica', 12, 'bold'),
                     command=lambda: start(2), height=1, width=7)
    large_2.grid(row=1, column=4, pady=10)

    large_3 = Button(gui, text='3', fg='white', bg='grey', font=('Helvetica', 12, 'bold'),
                     command=lambda: start(3), height=1, width=7)
    large_3.grid(row=1, column=5, pady=10)

    large_4 = Button(gui, text='4', fg='white', bg='grey', font=('Helvetica', 12, 'bold'),
                     command=lambda: start(4), height=1, width=7)
    large_4.grid(row=1, column=6, pady=10)

    # start the GUI
    gui.mainloop()
