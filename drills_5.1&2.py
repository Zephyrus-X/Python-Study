#5-1：条件测试
car = 'sakura'
print ("Is car == 'sakura'? I predict True.")
print (car == 'sakura')
print ("\nIs car == 'bmw'? I predict False")
print (car == 'bmw')

age_0 = 22
age_1 = 18
print (age_0 > 20 and age_1 < 20)
print (age_0 <= 20 or age_1 >= 18)

bikes = ['A', 'b', 'C', 'd']
bike = 'A'
if bike not in bikes:
    print ('Ture')
else:
    print ('False')

user_names = ['Abc', 'abdw', 'siwjd', 'sdsajhiwoq']
use_name = 'abc'
if use_name.upper() or use_name.title() in user_names:
    print ('You should try another user name.')
else:
    print ('That is really a good name!')


