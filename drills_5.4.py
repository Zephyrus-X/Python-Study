#5-8：以特殊方式跟管理员打招呼
names = ['admin', 'abcd', 'dfvg', 'fjie', 'dsnao']
for name in names:
    if name == 'admin':
        print (f"Hello {name}, would you like to see a status report?")
    else:
        print (f"Hello {name}, thank you for logging in again")

#5-9：处理没有用户的情形
names = []
if names:
    for name in names:
        if name == 'admin':
            print (f"Hello {name}, would you like to see a status report?")
        else:
            print (f"Hello {name}, thank you for logging in again")
else:
    print ("We need to find some users!")

#5-10：检查用户名
current_users = ['admin', 'abcd', 'DFVG', 'fjie', 'dsnao', 'shdisq']
current_users_copy = [users.lower() for users in current_users]
new_users = ['ABCD', 'dfvg', 'sjdiww', 'sjiodoo', 'wqoooo']
new_users_copy = [users.lower() for users in new_users]
for user in new_users_copy:
    if user in current_users_copy:
        print (f"Sorry, the user name {user} is unavailable.")
    else:
        print (f"Good, this user name {user} is available.")

#5-11：序数
numbers = list(range (1, 10))
for number in numbers:
    if number == 1:
        print (f"{number}st")
    elif number == 2:
        print (f"{number}nd")
    elif number == 3:
        print (f"{number}rd")
    else:
        print (f"{number}th")






