from email import message
from pyexpat import XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE

#2.3 2.4 练习，涉及内容：变量，字符串
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