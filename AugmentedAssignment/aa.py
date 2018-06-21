number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The Number is {}".format(newNumber))

x = 23
x += 1
print(x)  # 24

x -= 4
print(x)  # 20

x *= 5
print(x)  # 100

x /= 4
print(x)  # 25.0

x **= 2
print(x)  # 625.0

x %= 60
print(x)  # 25.0

greeting = "Good "
greeting += "morning "
print(greeting)  # Good morning

greeting *= 5
print(greeting)  # Good morning Good morning Good morning Good morning Good morning
