# # No.1
def info():
    a = input('Please enter your name: ')    #a represents the input
    b = int(input('Please enter your age: ')) # b represents the age
    c = int(input('Enter current year:  '))   #its the input for the current year
    d = input((c - b)+100) #to get the year that the person truns 100  subtract the current year from the age and add 100

    print( a + " will become 100 years old in " + d)
info()

# # No.2
s = int(input('Enter a number: ')) 
p = int((s / 2))
if p % 2 == 0:
    print('the  number you chose is an even number')
else:
    print('the number you chose is an odd number')


# # No.3
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for items in list:
    if items < 5:
        print (items)


# # No.4   
x = int(input('Enter a number: '))
print ("The divisors are: ")
for y in range(1,x+1):
    if(x % y == 0):
        print (y)
    
#No.5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [value for value in a if value in b] 
print (c)

#No.6
f= str(input('Enter a string here: '))
d_str = 'dad'
d_str = d_str.casefold()
rev_str = reversed(d_str)
if list(d_str) == list(rev_str):
    print('this word is a palindrome') 
else:
    print('this word is not a palindrome') 

#No.7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [items for items in a if items % 2 == 0]
print(b)

#No.8
e =["rock", "paper", "scissors"]
import sys
player1 = input("What's your name?")
player2 = input("And your name?")
player1_answer = input("%s, do yo want to choose rock, paper or scissors?" % player1)
player2_answer = input("%s, do you want to choose rock, paper or scissors?" % player2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(player1_answer, player2_answer))


#No.9
z = [1,2,3,4,5,6,7,8,9]
guess = input('Guess any number here:')
a += 1

#  count += 1
if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct!")
    print("it took you",count,"tries!")



    