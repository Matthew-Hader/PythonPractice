def bmiCalculator(weight, height):
    return weight / (height ** 2)

def bmiResults(bmi):
    if bmi >= 30:
        return "obese"
    elif bmi >= 25:
        return "over"
    elif bmi >= 18.5:
        return "normal"
    else:
        return "under"

results = ""
inputs = input("Enter number of people: ")
for i in range(int(inputs)):
    data = input("Enter weight (kg) and height (m): ")
    weight = int(data.split()[0])
    height = float(data.split()[1])

    results += f"{bmiResults(bmiCalculator(weight, height))} "

print("answer:")
print(results)
