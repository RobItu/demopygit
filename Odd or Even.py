
#This will be an Odd or Even game, where the user inputs a number and the program responds whether it's even or odd.
Name = input('What is your name?\n')
print('Hello ' + Name + ', please input any number')
Number = int(input())
if Number%2 == 0:
    print('Your number is an even number!')
else:
    print('Your number is an odd number!')
print('Great, now we are going to play a game. Guess the number 1 or 2, I will also randomly input a 1 or 2')
print('The addition of our two numbers will determine the winner (me if odd) and the loser (you if even)')
number2=input('What number do you choose?\n')
random=number.random()

