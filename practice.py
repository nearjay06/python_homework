
def info():
    a = input('Please enter your name: ')    #a represents the input
    b = int(input('Please enter your age: ')) # b represents the age
    c = int(input('Enter current year:  '))   #its the input for the current year
    d = input((c - b)+100) #to get the year that the person truns 100  subtract the current year from the age and add 100

    print( a + " will become 100 years old in " + d)
info()


s = int(input('Enter a number: ')) 
p = int((s / 2))
if p % 2 == 0:
    print('the  number you chose is an even number')
else:
    print('the number you chose is an odd number')
        
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for items in list:
    if items < 5:
        print (items)
    
x = int(input('Enter a number: '))
print ("The divisors are: ")
for y in range(1,x+1):
    if(x % y == 0):
        print (y)
    
        