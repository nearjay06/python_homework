#21
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.txt)
soup.find_all(class_="story-heading")
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a)
    else: 
        print(story_heading)

#22
names.txt = [Darth,Luke,Darth,Lea,Darth,Lea,Lea,Luke,Darth,Lea,Darth,Darth,Lea,Lea,Darth,Lea,Darth,Lea]
counter_dict = {}
with open('names.txt') as f:
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


#24


#25


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

#29

#30
import random

with open('sowpods.txt') as f:
    words = list(f)
print(random.choice(words).strip())
    
#31

#32

#33
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