import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for i in my_randoms:
        if i == number:
            the_numbers_match = True

    if the_numbers_match == True:
        print(f'the list contains {number}')

    # Does my_randoms contain number? Change the boolean.

    print(f'{number} is in the random list')


planets_list = ["Mercury", "Mars"]
second_planet = planets_list[1]

planets_list.append("Jupiter")
planets_list.append("Saturn")

planets_list.extend(["Uranus", "Neptune"])

planets_list.insert(1, "Earth")

print(planets_list)
