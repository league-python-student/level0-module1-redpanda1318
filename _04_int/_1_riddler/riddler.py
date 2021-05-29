"""
* Write a python program that asks the user a minimum of 3 riddles.


* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct


"""


import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

from tkinter import simpledialog

score = 0

riddle1 = simpledialog.askstring('Title', "What can you keep after giving to someone?")
if riddle1 == 'your word':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer is your word")
riddle2 = simpledialog.askstring('Title', "What goes through cities and fields but never moves?")
if riddle2 == 'roads':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was roads")
riddle3 = simpledialog.askstring('Title', "If you drop me I'm sure to crack, but give me a smile and I'll always smile back. What am I?")
if riddle3 == 'mirror':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was mirror")
riddle4 = simpledialog.askstring('Title', "The more you take, the more you leave behind. What are they?")
if riddle4 == 'footsteps':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was footsteps")
riddle5 = simpledialog.askstring('Title', "What is the end of everything?")
if riddle5 == 'g':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was g")
riddle6 = simpledialog.askstring('Title', "What word is pronounced the same if you take away four of its five letters?")
if riddle6 == 'queue':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was queue")
riddle7 = simpledialog.askstring('Title', "What 4 letter word can be written forward, backward, upside down, and can still be read from left to right?")
if riddle7 == 'NOON':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was NOON")
riddle8 = simpledialog.askstring('Title', "If there are three apples and you take away two, how many apples do you have?")
if riddle8 == 'two':
    print("Congratulations, You got that right!")
    score = score+1

else:
    print("Incorrect, the answer was two")

print("Your score was" + str(score))







