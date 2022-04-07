from email import message

#f format字符串，在字符串中使用变量
first_name = 'xinyu'
last_name = 'zhu'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print (message)

#\t 制表符 \n换行符
print ("languages:\n\tChinese\n\tEnglish\n\tJapanese\n\tDutch")
