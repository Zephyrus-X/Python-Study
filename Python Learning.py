from email import message

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