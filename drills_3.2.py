#3-4
dinner_guests = ['xinyu', 'Ivy', 'dage', 'zhan']
message = f"dinner guests are {dinner_guests}"
print (message)

#3-5
popped_guests = dinner_guests.pop(-1)
message_1 = f"the guest that can not arrive is {popped_guests}"
print (message_1)
dinner_guests.append('bo')
message_2 = f"The new invitation is {dinner_guests}"
print (message_2)

#3-6
message_3 = 'we will provide a bigger table'
dinner_guests.insert(0, 'Yu')
dinner_guests.insert(3, 'A')
dinner_guests.insert(6, 'B')
message_4 = f"invitation list:\n{dinner_guests}"
print (message_3)
print (message_4)

#3-7
emergence = 'Sorry, due to the delay of table delivery, I have to reduce the invitation to two people.'
print (emergence)
popped_guests_1 = dinner_guests.pop(0)
print (f"Dear {popped_guests_1}, sorry, I cannot invite you this time, see you next time.")
popped_guests_2 = dinner_guests.pop(0)
print (f"Dear {popped_guests_2}, sorry, I cannot invite you this time, see you next time.")
popped_guests_3 = dinner_guests.pop(0)
print (f"Dear {popped_guests_3}, sorry, I cannot invite you this time, see you next time.")
popped_guests_4 = dinner_guests.pop(0)
print (f"Dear {popped_guests_4}, sorry, I cannot invite you this time, see you next time.")
popped_guests_5 = dinner_guests.pop(0)
print (f"Dear {popped_guests_5}, sorry, I cannot invite you this time, see you next time.")
print (f"Dear {dinner_guests[0]}, you are still invited.")
print (f"Dear {dinner_guests[1]}, you are still invited.")
del dinner_guests [0]
del dinner_guests [0]
print (f"final invitation list: {dinner_guests}")


