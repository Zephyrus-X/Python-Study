#6-7：人们
people_1 = {'first_name':'xinyu', 'last_name': 'zhu', 'age': '23', 'city':'Leeds'}
people_2 = {'first_name':'Ivy', 'last_name': 'Cao', 'age': '25', 'city':'Leeds'}
people_3 = {'first_name':'Yu', 'last_name': 'Wang', 'age': '23', 'city':'Leeds'}
friends = [people_1, people_2, people_3]
for friend in friends:
    print (friend)

#6-8：宠物

#6-9：喜欢的地方
favorite_place = {}
favorite_place ['Xinyu'] = 'Leeds', 'York', 'Newcastle'
favorite_place ['Ivy'] = 'Paris', 'Italy', 'Newyork'
favorite_place ['Yu'] = 'Beijing', 'Shanghai', 'Hubei'
for names, places in favorite_place.items():
    print (f"{names} likes visiting:")
    for place in places:
        print (f"{place}")

#6-10：喜欢的数2
numbers = {'xinyu':['2', '3', '4'],
    'yu':['3', '5', '6'],
    'ivy':['4', '7', '88'],
    'dage': ['5', '21', '321'],
    'jjj': ['6', '23', '42']
    }
for a, b in numbers.items():
    print (f"{a}'s favorite number are:")
    for c in b:
        print (f"{c}")

#6-11：城市
cities = {}
cities ['Leeds'] = {'country' : 'UK',
    'population' : '2300000',
    'fact' : 'global',
    }
cities ['York'] = {'country' : 'UK',
    'population' : '1900000',
    'fact' : 'countryside',
    }
cities ['London'] = {'country' : 'UK',
    'population' : '23000000',
    'fact' : 'big',
    }
print (cities)
for cities_names, cities_info in cities.items():
    print (f"City name = {cities_names}")
    country = f"{cities_info ['country']}"
    population = f"{cities_info ['population']}"
    fact = f"{cities_info ['fact']}"
    print (f"Country belongging is {country}.")
    print (f"Population is {population}.")
    print (f"The fact of {cities_names} is '{fact}'.")
