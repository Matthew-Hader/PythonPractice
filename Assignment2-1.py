from string import digits, ascii_lowercase

#1.
print('Hello World'[8])
#2.
print('thinker'[2:5])
print('hello'[1]) #s[1] = e
#3.
print('Sammy'[2:]) #s[2:] = mmy

#4.
print(set('Mississippi'))

#5.
def removePunctuation(word):
    return ''.join(i for i in word.lower() if i in ascii_lowercase or i in digits)

var = input('Enter number of phrases: ')
num = 0
result = ''
while num < int(var):
    string = input('Enter phrase: ')
    string = removePunctuation(string)
    if(string == string[::-1]):
        result += 'Y '
    else:
        result += 'N '
    num += 1

print(result)
