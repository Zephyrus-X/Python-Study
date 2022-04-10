#4-10
squares = [value + 1 for value in range (0, 10)]
print (squares)
print (f'“The first three items in the list are:\n{squares [0:3]}”')
print (f'"Three items from the middle of the list are:\n{squares [4:7]}"')
print (f'“The last three items in the list are:\n{squares [7:]}”')

#4-11
Pizzas = ['AAA', 'BBB', 'CCC']
friend_pizzas = Pizzas[:]
Pizzas.append ('DDD')
friend_pizzas.append ('EEE')
print (f"My favorite pizzas are:\n")
for Pizza in Pizzas:
    print (Pizza)
print (f"'My friends' favorite pizzas are:\n")
for friend_pizza in friend_pizzas:
    print (friend_pizza)

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for value in my_foods:
    print (f"My favorite foods are: {value}")
for value in friend_foods:
    print(f"My friend's favorite foods are: {value}")

#4-13
foods_offer = ("apple", "banana", "oringe", "melon", "AAA")
for food in foods_offer:
    print (food)

foods_offer = ("apple", "CCC", "DDD", "melon", "AAA") 
for food in foods_offer:
    print (food)
