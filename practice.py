# # No.1
def info():
    a = input('Please enter your name: ')    #a represents the input
    b = int(input('Please enter your age: ')) # b represents the age
    c = int(input('Enter current year:  '))   #its the input for the current year
    d = input((c - b)+100) #to get the year that the person truns 100  subtract the current year from the age and add 100

    print( a + " will become 100 years old in " + d)
info()

# No.2
s = int(input('Enter a number: ')) 
p = int((s / 2))
if p % 2 == 0:
    print('the  number you chose is an even number')
else:
    print('the number you chose is an odd number')


#No.3
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for items in list:
    if items < 5:
        print (items)


#No.4   
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

import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1

if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct!")
    print("it took you",count,"tries!")

# No.10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [item for item in a if b]
print(c)

# No.11
x =[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
z = int(input('Enter a number: '))
for y in range(2, z):
    if(z % y == 1):
        print ('This is a prime number') 
    elif (z % 1 == z):
        print('This is a prime number')
    else:
        print('This is not a prime number')

# # No.12

a = [5,10,15,20,25,30,35,40]
b = (a[0],a[-1])
print(b)

#No.13

xterms = 11

x1 = 0
x2 = 1
compute = 0

if xterms <= 0:
    print ('Enter a positive number')
elif xterms == 1:
   print("Fibonacci sequence upto",xterms,":")
   print(x1)
else:
    print("Fibonacci sequence upto",xterms,":")
    while compute < xterms:
        print(x1)
        xth = x1 + x2
        x1 = x2
        x2 = xth
        compute += 1


#No.14

def new_list():

    s = [1,2,2,3,4,4,5,6,6,7,8,8,9,9,10]
    s = list(dict.fromkeys(s))
    print(s)

new_list()

#No.15

z = 'Hello everyone' 
reversed =''.join(reversed(z)) 
print(reversed) 
    

#No.16
import random
import string
def password(stringLength=10):
    letters = string.ascii_lowercase + string.punctuation + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
print (password() )
print (password(10))

#No.17
# import requests
# from bs4 import BeautifulSoup
 
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)
 
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())


#No.18
import random

def compare_numbers(number, user_guess):
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True 
    number = str(random.randint(0,9999)) 
    guesses = 0

    print("The game is called Cowbull!") 
    print("I will say a number, and you have to guess the numbers.")
    print("if the number is wrong, you get a cow. If it's right, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit to end the game.")

#No.19
# import requests
# from bs4 import BeautifulSoup

# base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)

# all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")

# for elem in all_p_cn_text_body[7:]:
#   print(elem.text)


#No.20
def list(ordered_list, numbers):
  for items in ordered_list:
    if items == numbers:
      print('Yes, the number is in the list a')
  print ('No, the number is not in the list a') 
  
if __name__=="__main__":
  a = [1,2,3,4,5,6,7]
  print(list(a, 5)) 
  print(list(a, 10)) 
  
