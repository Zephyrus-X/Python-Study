#3-8
from email import message
visiting_cities = ['London', 'Hongkong', 'Tokyo', 'Edinburgh', 'Leeds']
print (f"The cities that I want to visit are \n{visiting_cities}")
print (sorted(visiting_cities))
print (visiting_cities)
print (sorted(visiting_cities, reverse=True))
print (visiting_cities)
visiting_cities.reverse()
print (visiting_cities)
visiting_cities.reverse()
print (visiting_cities)
visiting_cities.sort()
print (visiting_cities)
visiting_cities.sort(reverse=True)
print (visiting_cities)

#3-9
dinner_guests = ['xinyu', 'Ivy', 'dage', 'zhan']
dinner_guests.insert(0, 'Yu')
dinner_guests.insert(3, 'A')
dinner_guests.insert(6, 'B')
len(dinner_guests)
message = f"we have invited {len(dinner_guests)} guests to come tonight."
print (f"The guests'list:\n {dinner_guests}")
print (message)