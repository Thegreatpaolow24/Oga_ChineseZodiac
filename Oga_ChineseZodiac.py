year = int(input("Enter your birth year: "))

zodiac_animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]

if 1900 <= year <= 2099:
    zodiac_index = (year - 1900) % 12

    if zodiac_index == 0:
        zodiac_sign = "Monkey"
    elif zodiac_index == 1:
        zodiac_sign = "Rooster"
    elif zodiac_index == 2:
        zodiac_sign = "Dog"
    elif zodiac_index == 3:
        zodiac_sign = "Pig"
    elif zodiac_index == 4:
        zodiac_sign = "Rat"
    elif zodiac_index == 5:
        zodiac_sign = "Ox"
    elif zodiac_index == 6:
        zodiac_sign = "Tiger"
    elif zodiac_index == 7:
        zodiac_sign = "Rabbit"
    elif zodiac_index == 8:
        zodiac_sign = "Dragon"
    elif zodiac_index == 9:
        zodiac_sign = "Snake"
    elif zodiac_index == 10:
        zodiac_sign = "Horse"
    else:
        zodiac_sign = "Sheep"

    print(f"The Chinese zodiac sign for the year {year} is {zodiac_sign}.")
else:
    print("Invalid year")
