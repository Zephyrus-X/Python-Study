#5-3：外星人颜色
from mailbox import Babyl


alien_color = 'red'
if alien_color == 'green':
    score = 5
else:
    score = 0
print (f"You just killed an alien in {alien_color} and got {score} scores!")

alien_color = 'green'
if alien_color == 'green':
    score = 5
else:
    score = 0
print (f"You just killed an alien in {alien_color} and got {score} scores!")

#5-4：外星人颜色2
alien_color = 'green'
if alien_color == 'green':
    score = 5
else:
    score = 10
print (f"You just killed an alien in {alien_color} and got {score} scores!")
alien_color = 'red'
if alien_color == 'green':
    score = 5
else:
    score = 10
print (f"You just killed an alien in {alien_color} and got {score} scores!")

#5-5：外星人颜色3
alien_color = 'red'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
print (f"You just killed an alien in {alien_color} and got {score} scores!")

#5-6：人生的不同阶段
age = 23
if age < 2:
    states = 'Baby'
elif age < 4:
    states = 'infant'
elif age < 13:
    states = 'Chind'
elif age < 20:
    states = 'teens'
elif age < 65:
    states = 'Adult'
else:
    states = 'Olders'
print (f"This person is now a/an {states}.")

#5-7：喜欢的水果
favorite_fruits = ['apple', 'banana', 'melon']
favorite_fruit = 'apple'
if favorite_fruit in favorite_fruits:
    print (f'you really like {favorite_fruit}')
else:
    print ("Don't you like apple, banana, and melon?")
