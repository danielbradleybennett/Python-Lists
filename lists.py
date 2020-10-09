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
planets_list.insert(2, "Venus")

planets_list.append("Pluto")

print(planets_list)

rocky_planets = list()
rocky_planets = planets_list[0:5]

print(rocky_planets)

del planets_list[8]

print(planets_list)

spacecraft = [
    ("Nemesis", "Mars"),
    ("Leviathan", "Earth"),
    ("Jacob's Ladder", "Venus"),
    ("Columbus", "Jupiter"),
    ("Terra", "Saturn"),
    ("Exodus", "Neptune"),

]

for planet in planets_list:
    visited = False
    vis = f'{planet} was visited by '
    for tuple in spacecraft:
        if tuple[1] == planet:
            vis += f'{tuple[0]}'
            visited = True

    else:
        vis = vis[slice(-2)] + f'.'

    if visited:
        print(vis)
    else:
        print(f'Nobody visiting {planet}.')
