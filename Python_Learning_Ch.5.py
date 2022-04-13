#第 5 章 if 语句
#5.1 一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
        print (car.title())

#5.2 条件测试 每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式称为条件测试
#5.2.1 检查是否相等
car = 'bmw'
car == 'bmw'
#5.2.2 检查是否相等时忽略大小写
car = 'Audi'
car.lower() == 'audi'
True
car
'Audi'
#5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchoives': #要判断两个值是否不等，可结合使用惊叹号和等号（!= ）
    print ('Hold the anchoives!')
#5.2.4 数值比较
answer = 17
if answer != 42:
    print ("That is not the correct answer. Please try again!")
#条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于 （<, <=, >, >=)
#5.2.5 检查多个条件
    #a. 使用and 检查多个条件(同时满足)
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)
    #b. 使用or检查多个条件(至少一个条件满足)
age_0 >= 21 or age_1 >= 21
#5.2.6 检查特定值是否包含在列表中 (关键字in)
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print ("A")
else:
    print ('B')
#5.2.7 检查特定值是否不包含在列表中 (关键字not in)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print (f"{user.title()}, you can post a response if you wish.")
#5.2.8 布尔表达式
game_active = True
can_edit = False

#5.3 if 语句
#5.3.1 简单的if 语句
age = 19
if age >= 18:
    print ('You are old enough to vote!')
    print("Have you registered to vote yet?")
#5.3.2 if-else 语句
age = 17
if age >= 18:
    print ('You are old enough to vote!')
    print("Have you registered to vote yet?")
else:
    print ("Sorry, you are too young to vote.")
    print ("Please register to vote as soon as you turn 18!")
#5.3.3 if-elif-else 结构
age = 18
if age < 4:
    print ("Your admission cost is $0.")
elif age < 18:
    print ("Your admission cost is $25.")
else:
    print ("Your admission cost is $40.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print (f"Your admission cost is ${price}.")
#5.3.4 使用多个elif 代码块
age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 25
print (f"Your admission cost is ${price}.")
#5.3.5 省略else 代码块
age = 40
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 25
print (f"Your admission cost is ${price}.")
#5.3.6 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print ("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print ('Adding extra cheese')
print("\nFinished making your pizza!") #总之，如果只想执行一个代码块，就使用if-elif-else 结构；如果要执行多个代码块，就使用一系列独立的if语句。

#5.4 使用if 语句处理列表
#5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print ("Sorry, we are out of green peppers right now.")
    else:
        print (f"Adding {requested_topping}.")

print ("\n Finished making your pizza.")
#5.4.2 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print (f"Adding {requested_topping}")
    print ("Finished making your pizza.")
else:
    print ("Are you sure you want a plain pizza?")
#5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print (f"Adding {requested_topping}")
    else:
        print (f"Sorry, we don't have {requested_topping}.")
print ("\nFinished making your pizza!")
