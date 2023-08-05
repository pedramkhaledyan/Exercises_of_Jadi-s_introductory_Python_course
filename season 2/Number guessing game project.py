# Number guessing game project

from random import randint
# First, choose a number between 1 and 99 in your mind
a=1
b=99
Computer_guess=randint(a,b)
print(Computer_guess)
# 
y=input()
# Tell the computer whether the guessed number is correct or not.
# if you type d, means computer's guess is correct
while y!='d':
    # if you type k, means computer should guess a smaller number than his current guess
    if y=='k':
        b=Computer_guess-1
        Computer_guessx=randint(a,b)
        print(Computer_guess)
        y=input()
    # if you type b, means computer should guess a bigger number than his current guess
    elif y=='b':
        a=Computer_guess+1
        Computer_guess=randint(a,b)
        print(Computer_guess)
        y=input()

print('right guess')

# The educational point of this program for me: first should define 3 variable for this project.2 variable for randint and a variable for computer's guess.according to the letter that the user enters, the computer's guess must be replaced in the variable a or b. 
# If we only use two variables and replace the computer's guess according to the user's input letter in one of these two variables, the number guess range will change every time and the game will end later.
