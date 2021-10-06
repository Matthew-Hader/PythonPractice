names = ["Matthew", "Bob", "Alfred", "Megan", "Austin", "Oprah"]
print(names)

def isCrowded(list):
    if len(list) > 5:
        return "There is a mob in the room"
    elif len(list) > 2:
        return "The room is crowded"
    elif len(list) > 0:
        return "The room is not crowded"
    else:
        return "The room is empty"

result = isCrowded(names)
print(result)

names.pop()
names.pop()
print(names)
result = isCrowded(names)
print(result)

names.pop()
names.pop()
print(names)
result = isCrowded(names)
print(result)

names.pop()
names.pop()
print(names)
result = isCrowded(names)
print(result)
