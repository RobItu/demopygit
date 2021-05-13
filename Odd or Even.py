
#This will be an Odd or Even game, where the user inputs a number and the program responds whether it's even or odd.
Name = input('What is your name?\n')
print('Hello ' + Name + ', please input any number')
Number = int(input())
if Number%2 == 0:
    print('Your number is an even number!')
else:
    print('Your number is an odd number!')

