#第 4 章 操作列表
#4.1 遍历整个列表
magicians = ['alice', 'david', 'carolina'] #需要对列表中的每个元素都执行相同的操作时，可使用Python中的for循环
for magician in magicians:
    print (magician) #对于列表magicians 中的每位魔术师，都将其名字打印出来
#4.1.1 深入研究循环
#编写for循环时，可以给依次与列表中每个值相关联的临时变量指定任意名称。然而，选择描述单个列表元素的有意义名称大有裨益。
#4.1.2 在for循环中执行更多操作
    print (f"{magician.title()}, that was a great trick!") #在for 循环中，想包含多少行代码都可以
    print (f"I can't wait to see your next trict, {magician.title()}!\n")
#4.1.3 在for循环结束后执行一些操作
print("Thank you, everyone. That was a great magic show!")

#4.2 避免缩进错误
#4.2.1 忘记缩进
#4.2.2 忘记缩进额外的代码行
#4.2.3 不必要的缩进
#4.2.4 循环后不必要的缩进
#4.2.5 遗漏了冒号

#4.3 创建数值列表
#4.3.1 使用函数range()
for value in range (1, 5): #range() 让你能够轻松地生成一系列数
    print (value) #range()只打印数1～4。这是编程语言中常见的差一行为的结果。
for value in range (6):
    print (value)
#4.3.2 使用range() 创建数字列表
numbers = list(range(1,6)) #要创建数字列表，可使用函数list() 将range() 的结果直接转换为列表。
print (numbers)
even_numbers = list(range(2,11,2)) #使用函数range() 时，还可使用第三个参数来指定步长，如一步加2。
print (even_numbers)
#如何创建一个列表，其中包含前10个整数（1～10）的平方呢？
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print (squares)
#精简版
squares = []
for value in range (1, 11):
    squares.append (value ** 2)
print (squares)
#4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] #最大值、最小值和总和
print (min (digits))
print (max (digits))
print (sum (digits))
#4.3.4 列表解析 #将for 循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value ** 2 for value in range (1, 11)]
print (squares)

#4.4 使用列表的一部分
#4.4.1 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players [0:3]) 
print (players[:4]) #由于没有指定起始索引，Python从列表开头开始提取
print (players[2:])
print (players[-3:]) #负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任意切片。
print (players [0:4:2]) #可在表示切片的方括号内指定第三个值。这个值告诉Python在指定范围内每隔多少元素提取一个。
#4.4.2 遍历切片
print("Here are the first three players on my team:")
for player in players[0:3]: #要遍历列表的部分元素，可在for 循环中使用切片
    print (player.title())
#4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:] #要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）
my_foods.append('icecream')
friend_foods.append('apple')
print (f'My favorite foods are:\n{my_foods}')
print (f"\nMy frinend's favorite foods are {friend_foods}")

#4.5 元组  Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组
#4.5.1 定义元组
dimensions = (200, 50) # 无法修改元组的值：dimensions[0] = 250
print (dimensions [0])
print (dimensions [1])
my_t = (3,) #元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号
#4.5.2 遍历元组中的所有值
for dimension in dimensions:
    print (dimension)
#4.5.3 修改元组变量
print ('Original dimensions:')
for dimension in dimensions:
    print (dimension)
dimensions = (400, 100)
print ("\nmodified dimensions:")
for dimension in dimensions:
    print (dimension)

#4.6 设置代码格式
#4.6.1 格式设置指南: Python改进提案 （Python EnhancementProposal，PEP）
#4.6.2 缩进: PEP 8建议每级缩进都使用四个空格
#4.6.3 行长: 很多Python程序员建议每行不超过80字符;PEP 8还建议注释的行长不应超过72字符
#4.6.4 空行
