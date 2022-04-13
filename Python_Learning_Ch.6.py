#第 6 章 字典
#6.1 一个简单的字典
alien_0 = {'color': 'green', 'point': 5}
print (alien_0['color'])
print (alien_0['point'])

#6.2 使用字典
#在Python中，字典 是一系列键值对 。每个键 都与一个值相关联，你可使用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。
#6.2.1 访问字典中的值
new_point = alien_0['point']
print (f"You just earned {new_point} points!")
#6.2.2 添加键值对
alien_0 ['x_position'] = 0
alien_0 ['y_position'] = 25
print (alien_0)
#6.2.3 先创建一个空字典
alien_1 = {}
alien_1 ['color'] = 'red'
alien_1 ['point'] = 10
print (alien_1)
#6.2.4 修改字典中的值
alien_1 ['color'] = 'yellow'
print (alien_1)

#例子
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_3 ['speed'] == 'slow':
    x_increment = 1
elif alien_3 ['speed'] == 'medium':
    x_increment = 2
else:
# 这个外星人的移动速度肯定很快。
    x_increment = 3
# 新位置为旧位置加上移动距离。
alien_3 ['x_position'] = alien_3['x_position'] + x_increment
print (f"New position: {alien_3 ['x_position']}")

#6.2.5 删除键值对
del alien_3 ['y_position'] #可使用del 语句将相应的键值对彻底删除
print (alien_3)
#6.2.6 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages ['sarah'].title()
print (f"Sarah's favorite language is {language}.")
#6.2.7 使用get() 来访问值
alien_4 = {'color': 'green', 'speed': 'slow'}
point_value = alien_4.get ('point', 'No point value assigned.')
print (point_value) #如果指定的键有可能不存在，应考虑使用方法get() ，而不要使用方括号表示法。

#6.3 遍历字典
#6.3.1 遍历所有键值对
user_0 = {'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for k, value in user_0.items(): #for 语句的第二部分包含字典名和方法items() ，它返回一个键值对列表。
    print (f"\nKey: {k}")
    print (f"Value: {value}")
#6.3.2 遍历字典中的所有键 在不需要使用字典中的值时，方法keys() 很有用。
for name in favorite_languages.keys(): #遍历字典时，会默认遍历所有的键(keys可有可无)
    print (name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print (f"Hi, {name.title()}")
    if name in friends:
        language = favorite_languages[name].title() #为获悉朋友喜欢的语言，我们使用了字典名，并将变量name 的当前值作为键
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys(): #还可使用方法keys() 确定某个人是否接受了调查
    print("Erin, please take our poll!")
#6.3.3 按特定顺序遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted (favorite_languages.keys()): #要以特定顺序返回元素，一种办法是在for 循环中对返回的键进行排序。为此，可使用函数sorted()
    print (f"Hello {name.title()}, thank you for taking the poll.")
#6.3.4 遍历字典中的所有值
print ("The following languages have been mentioned:")
for language in favorite_languages.values(): #.values()这种做法提取字典中所有的值，而没有考虑是否重复。
    print (language.title())

for language in set (favorite_languages.values()): #为剔除重复项，可使用集合（set）。集合 中的每个元素都必须是独一无二的
    print (language.title())
#可使用一对花括号直接创建集合，并在其中用逗号分隔元素：
languages = {'python', 'ruby', 'python', 'c'}
print (languages)

#6.4 嵌套 将一系列字典存储在列表中，或将列表作为值存储在字典中
#6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print (alien)

#例子
# 创建一个用于存储外星人的空列表。
aliens = []
# 创建30个绿色的外星人。
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前5个外星人。
for alien in aliens [:5]:
    print (alien)
print ('...')

# 显示创建了多少个外星人。
print(f"Total number of aliens: {len(aliens)}")

#6.4.2 在字典中存储列表
# 存储所点比萨的信息
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
    }
# 概述所点的比萨
print (f"You ordered a {pizza['crust']}-crust pizza "
        "with a following toppings:")
for topping in pizza ['toppings']:
    print (f"{topping}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print (f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print (f"\t{language.title()}")
    else:
        print (f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print (f"\t{language.title()}")
#6.4.3 在字典中存储字典
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
    }
for user_name, user_info in users.items():
    print (f"\nUsername: {user_name}")
    full_name = f"{user_info['first']} {user_info ['last']}"
    location = user_info['location']
    print (f"Full name = {full_name.title()}")
    print (f"Location: {location.title()}")

