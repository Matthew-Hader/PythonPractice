#2.
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Berry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

def func(list):
    return(map(lambda row: (row[0], (row[2] * row[3])) if (row[2] * row[3]) > 100 else (row[0], 10 + (row[2] * row[3])), orders))

for item in func(list):
    print(item)

#3. 
orders = [
    [34587, (1, 4, 40.95), (2, 2, 56.80)],
    [98762, (3, 10, 32.95)],
    [77226, (3, 1, 32.95), (1, 2, 40.95), (2, 1, 56.80)],
    [88112, (4, 3, 24.99), (1, 1, 40.95)]
]

def total(orders):
    result = []
    for i in orders:
        total = 0

        for j in range(1, len(i)):
            total += (i[j][1] * i[j][2])

        result.append((i[0], total))

    return result

for item in total(orders):
    print(item)
