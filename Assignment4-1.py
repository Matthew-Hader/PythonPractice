#1.
def hello():
    print("Hello World")

hello()

#2.
def greet(name):
    print("Hi, my name is", name)

greet("Kevin")

#3.
def zPicks(x, y, z):
    if z is True:
        print(x)
    else:
        print(y)

zPicks("hello", "goodbye", True)
zPicks("hello", "goodbye", False)

#4.
def func4(x, y):
    return x * y

print(func4(2, 25))

#5.
def isEven(num):
    if(num % 2 == 0):
        return True
    else:
        return False

print(isEven(5))
print(isEven(4))

#6.
def func6(x, y):
    if x <= y:
        return False
    else:
        return True

print(func6(2, 5))
print(func6(5, 5))
print(func6(6, 5))

#7.
def func7(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(func7(1, 2, 3, 4, 5))

#8.
def func8(*args):
    return [x for x in args if x % 2 == 0]

print(func8(1, 2, 3, 4, 5, 6))

#9.
def func9(string):
    result = []
    for i in range(len(string)):
        if i % 2 == 0:
            result.append(string[i].upper())
        else:
            result.append(string[i].lower())

    return ''.join(result)

print(func9("Test String"))

#10.
def func10(x, y):
    res = 0
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            return x
        else:
            return y
    else:
        if x > y:
            return x
        else:
            return y

print(func10(10, 20))
print(func10(20, 10))
print(func10(11, 21))
print(func10(20, 11))

#11.
def func11(str1, str2):
    if str1[0].lower() == str2[0].lower():
        return True
    else:
        return False

print(func11("Saturday", "Salt"))
print(func11("Saturday", "Malt"))
print(func11("Saturday", "salt"))

#12.
def func12(num):
    diff = num - 7
    return 7 + (2 * diff)

print(func12(12))
print(func12(3))

#13.
def func13(str):
    result = []
    for i in range(len(str)):
        if i == 0 or i == 3:
            result.append(str[i].upper())
        else:
            result.append(str[i])

    return ''.join(result)

print(func13("Test String"))
print(func13("sample all lower case string"))
print(func13("UPPERCASE"))
