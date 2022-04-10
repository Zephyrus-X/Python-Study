#Python学习-2022.04.07
#f format字符串，在字符串中使用变量
first_name = 'xinyu'
last_name = 'zhu'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print (message)
#\t 制表符 \n换行符
print ("languages:\n\tChinese\n\tEnglish\n\tJapanese\n\tDutch")
#.rstrip() 删除右侧空白. .lstrip()删除左侧空白 .strip()删除双侧空白
#e.g. language = language.rstrip()
#涉及内容：2.2变量，2.3字符串
first_name = "eric"
full_name = f"{first_name}"
message = f"Hello {full_name.title()}, would you like to learn some Python today?"
print (message)
name_1 = 'xinyu'
message_1 = f'My name is {name_1.upper()}'
message_2 = 'It is nice to meet you!'
print (message_1) 
print (message_2)
famous_name = 'albert einstein'
message_4 = f"{famous_name.title()} once said:\n\t'A person who never made a mistake never tried anything new."
print (message_4)

#以下内容为2.4数
#2.4.1 整数
print (3+2)
print (3**3)
#2.4.2 浮点数 (结果包含的小数位数可能是不确定的)
#2.4.3 整数与浮点数 （将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除）
print (4/2)
#2.4.4 数中的下划线
universe_age = 14_000_000_000_000
print (f"universe age:{universe_age}")
#2.4.5 同时给多个变量赋值
x, y, z = 0, 0, 0
#2.4.6 常量 (在代码中，要指出应将特定的变量视为常量，可将其字母全部大写)
MAX_CONNECTIONS = 5000
print (MAX_CONNECTIONS)

#3.1 列表
bycicles = ['cannondale', 'redline', 'specialized']
print (bycicles)
#3.1.1 访问列表元素
print (bycicles[0]) #索引从0而不是1开始
print (bycicles[1].title()) #还可以对任意列表元素调用字符串
#索引指定为-1 ，可让Python返回最后一个列表元素(-2,-3...)
print (bycicles[-1].title())
#使用列表中的各个值
message_5 = f"My first bycicle was a {bycicles[-1].title()}."
print (message_5)

#3.2 修改、添加和删除元素

#3.2.1 修改列表元素
motorcycles = ['honda', 'yomaha', 'suzuki']
print  (motorcycles[0])
motorcycles[0] = 'ducati'
print (motorcycles[0])
print (motorcycles)

#3.2.2 在列表中添加元素
#01. 在列表末尾添加元素
motorcycles[0] = 'honda'
motorcycles.append ('ducati')#最简单的方式是将元素附加(append)到列表
print (motorcycles)
color = []
color.append ('red')#方法.append() 让动态地创建列表易如反掌
color.append ('blue')
color.append ('black')
color.append ('white')
print (color) #为控制用户，可首先创建一个空列表，用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中
#02. 在列表中插入元素, 使用方法.insert() 可在列表的任何位置添加新元素
motorcycles.insert (0, 'bmx') #数字表示插入值得位置
print (motorcycles)

#3.2.3 从列表中删除元素 (2022.04.08)
#01. 使用del 语句删除元素
del motorcycles[0] #如果知道要删除的元素在列表中的位置，可使用del语句
print (motorcycles)
#02. 使用方法pop()删除元素
popped_motorcycles = motorcycles.pop()
print (popped_motorcycles)
#03. 弹出列表中任何位置处的元素 
popped_motorcycles = motorcycles.pop(0) #可以使用pop() 来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引即可。
print (popped_motorcycles)
#04. 根据值删除元素
motorcycles.remove ('yomaha') #如果只知道要删除的元素的值，可使用方法remove()
print (motorcycles)
cars = ['bmw', 'audi', 'benci', 'toyoda', 'honda']
print (cars)
too_expensive = 'bmw'
cars.remove(too_expensive) #使用remove() 从列表中删除元素时，也可接着使用它的值
print (cars)
print (f'\nA {too_expensive.title()} is too expensive for me.')

#3.3 组织列表 (2022.04.09)
#3.3.1 使用方法sort()对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #永久性地修改列表元素的排列顺序
print (cars)
cars.sort(reverse=True)  #还可以按与字母顺序相反的顺序排列列表元素，只需向sort()方法传递参数reverse=True即可
print (cars)
#3.3.2 使用函数sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print ("Here is the original list:")
print (cars)
print ("\nHere is the sorted list:")
print (sorted(cars, reverse=True)) #也可以在此添加reverse参数
print ("\nHere is the original list again:")
print (cars)
#3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
cars.reverse() #要反转列表元素的排列顺序，可使用方法reverse()
print (cars) #永久性修改，要恢复的话只需再次reverse()
cars.reverse()
print (cars)
#3.3.4 确定列表的长度
len(cars) #使用函数len() 可快速获悉列表的长度
ramianing_cars = len(cars)
print (ramianing_cars)
