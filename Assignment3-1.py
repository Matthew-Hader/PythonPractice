#1.
string = ''
for n in range(1500, 2700):
    if n % 7 == 0 and n % 5 == 0:
        string += (str(n) + ', ')

print(string)

#2.
temp_type = input("Convert to F or C: ")
temp = input("Enter Temperature: ")
if temp_type == "F":
    fahr = ((9 * int(temp))/ 5) + 32
    print(str(temp) + "°C is " + str(fahr) + "°F")
if temp_type == "C":
    cels = (5 / 9) * (int(temp) - 32)
    print(str(temp) + "°F is " + str(cels) + "°C")

#3.
import random

random = random.randint(1, 9)
correct = False
while correct == False:
    guess = input("Guess a number between  1 and 9: ")
    if random == int(guess):
        print("Well guessed!")
        correct = True
        break
    else:
        print("Incorrect. Guess again")

#4.
for i in range(5):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

#5.
word = input("Enter a word: ")
print(word[::-1])

#6.
sample = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = odd_count = 0
for value in sample:
    if(value % 2 == 0):
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers " + str(even_count))
print("Number of odd numbers " + str(odd_count))

#7.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print(item, " is of type ", type(item))

#8.
i = -1
while i < 6:
    i += 1
    if i == 3 or i == 6:
        continue
    print(i)
