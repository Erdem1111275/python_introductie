#Itereren over een lijst
i= 1

while(i != 31):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if result == "":
        result = i
    i += 1
    print(result)

#Breaks en continues
numbers = range(1, 100)

for number in numbers:
    is_prime = True
    
    for divisor in numbers:

        if number > divisor > 1:

            if number % divisor == 0:
                is_prime = False
                break

    if is_prime:
        print(number)

# Geneste lijsten
import random

# 1
bingo_number_total = 4 ** 2

numbers_all = list(range(1, 100))

random.shuffle(numbers_all)

bingo_numbers = numbers_all[:bingo_number_total]

bingo_card = list()

for i in range(4):
    card_row = list()

    for i in range(4):
        number = bingo_numbers.pop(0)
        card_row.append(number)
    bingo_card.append(card_row)

for row in bingo_card:
    print(row)

# 2
all_numbers = list(range(1, 100))

random.shuffle(all_numbers)

random_numbers = all_numbers[:50]

for number in random_numbers:

    for row in bingo_card:

        if number in row:
            number_index = row.index(number)
            row[number_index] = 0
            print(number)
            print(number_index)
        
for row in bingo_card:
    print(row)

# 3
bingo = False

for row in bingo_card:

    if sum(row) == 0:
        print("BINGO!")
        bingo = True
        break

if not bingo:
    for index in range(4):
        sum_index_row = sum(row[index] for row in bingo_card)

        if sum_index_row == 0:
            print("BINGO!")
            break

# while loops
numbers = range(1, 100)
number = ""

while number != ".":
    number = input("Geef een getal ")
    try:
        number = int(number)

        if number < 100:
            for divisor in numbers:
                if number > divisor > 1:
                    if number % divisor == 0:
                        print(f"{number} is een priemgetal")
                        break
            print(f"{number} is geen priemgetal")
        print("Geef een getal tot 100!")
    except:
        if number == ".":
            continue
