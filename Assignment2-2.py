
#1.
list = [1, 'word', 2.3]
print(list)

#2.
list2 = [1, 1, [1, 2]]
print(list2[2][1])

#3.
list3 = ['a', 'b', 'c']
print(list3[1:])

#4.
dict = {"monday": 1, "tuesday": 2,  "wednesday": 3,  "thursday": 4,  "friday": 5}
print(dict)

#5.
D = {'k1': [1, 2, 3]}
print(D['k1'][1])

#6.
list4 = [1, [2, 3]]
result = tuple(list4)
print(result)

#7.
set1 = set('Mississippi')
print(set1)

#8.
set1.add('X')
print(set1)

#9.
set2 = set([1, 1, 2, 3])
print(set2)

#10.
string = ''
for n in range(2000, 3200):
    if n % 7 == 0 and n % 5 != 0:
        string += (str(n) + ', ')

print(string)

#11.
def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i - 1)

num = input('Enter a number: ')
print(factorial(int(num)))

#12.
num = int(input('Enter a number: '))
d = {}
for i in range(1, num + 1):
    d[i] = i * i

print(d)

#13.
values = input('Enter comma separated integers: ')
list_nums = values.split(',')
tuple_nums = tuple(list_nums)
print(list_nums)
print(tuple_nums)

#14.
class GetAndPrintString(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

object = GetAndPrintString()
object.getString()
object.printString()
