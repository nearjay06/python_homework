#21
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html=r.text
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
soup.find_all(class_="story-heading")
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a)
    else: 
        print(story_heading)

#22
counter_dict = {}
with open('notepad.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

#23

prime_list = []
with open('one.txt') as primesfile:
	line = primesfile.readline()
	while line:
		prime_list.append(int(line))
		line = primesfile.readline()

other_list = []
with open('other.txt') as otherfile:
	line = otherfile.readline()
	while line:
		other_list.append(int(line))
		line = otherfile.readline()

overlap = []
for num in prime_list:
	if num in other_list:
		overlap.append(num)
		
print(overlap)

#24

def horizontal_line():
    print(" --- " * board_size)

def vertical_line():
    print("|   " * (board_size + 1))

if __name__ == "__main__":
    board_size = int(input("What size of game board? "))

    for index in range(board_size):
        horizontal_line()
        vertical_line()
    horizontal_line()


#25



def guess_the_number():
    # guess= 1
    counting =1

    a = [2,4,5,8,22,45,7,8,21,3]
    s = int(input('Guess the number I am thinking about : '))
    if s <= 5:
        print('You guessed a low number')
    elif s >= 22:
        print('You guessed a high number')
    else:
        print('You guessed the right number') 

# print("It took you",guess,"times to guess the right number")
guess_the_number()

# def guess():
#     i = 0
#     j = 100
#     m = 50
#     counter = 1
    
#     print ("Please guess a number")
#     condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
#     while condition != 1:
#         counter += 1
#         if condition == 0:
#             i = m + 1
#         elif condition == 2:
#             j = m - 1
#         m = (i + j) / 2
#         condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
#     print ("It took" , counter , "times to guess your number")
# guess()


#26




#27


#28
def large_numbers():
    u = [10,20,30,40,50,60,70,80,90,100]
    for numbers in u:
        if numbers >=10:
            print(u[1:4])
        if numbers >=30:
            print(u[3:6])
        if numbers >= 60:
            print(u[6:9])

large_numbers()

# #29

#30
import random

with open('sowpods.txt') as f:
    words = list(f)
print(random.choice(words).strip())
    
# #31

# #32

# #33
def birthdays():
    r = {'Olivia': '06/06/1988', 'Peter':'07/04/1981', 'Rachel':'09/09/1992', 'Luna':'06/05/2001', 'Jason':'01/02/1990'}
    print('Welcome to the birthday dictionary.These are the birthdays of:')
    for name in r:
        print(name)

    print('Whose birthday do you want to know?')
    name = input()
    if name in r:
        print('{}\'s birthday is {}.'.format(name, birthday[name]))
    else:
        print('Sorry, we don\'t have {}\'s birthday.'.format(name))

    
birthdays()

#34

import json 

with open("info.json", "r") as f:
    info = json.load(f)

if info["has_a_dog"]:
    print("{} has a dog".format(info["name"]))
else:
    print("{} does not have a dog".format(info["name"]))

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

if birthday["has_a_date"]:
    print("{} has a date".format(info["name"]))
else:
    print("{} does not have a birthdate in the set".format(info["name"]))

def birthdays():
    
    r = {'Olivia': '06/06/1988', 'Peter':'07/04/1981', 'Rachel':'09/09/1992', 'Luna':'06/05/2001', 'Jason':'01/02/1990'}
    print('Welcome to the birthday dictionary.These are the birthdays of:')
    for name in r:
        print(name) 

    print('Whose birthday do you want to know?')
    name = input()
    if name in r:
        print('{}\'s birthday is {}.'.format(name, birthday[name]))
    else:
        print('Sorry, we don\'t have {}\'s birthday.'.format(name))

      
birthdays()






