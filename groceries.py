#groceries.extend(groceries2+groceries3+ ['toilet paper'] + ['more beer'])
# - convert your infinte grocery item prompter 
#   - only accept 3 items 

groceries1 = []
while len(groceries1) < 3:
    item = input ('add something')
    groceries1.append(item)

groceries2 = []
while len(groceries2) < 3:
    item = input ('add something')
    groceries2.append(item)

groceries3 =groceries1+groceries2 
last_list = groceries3
print (last_list)

index_to_replace = int(input('what index to replace?'))

new_item = input ('what ist he new item?')

groceries3 [index_to_replace] = new_item

print(groceries3)

indexes = range(len(groceries3))
for i in indexes:
        item = groceries3[i]
        print(f'{i}: {item}')



"""indexes = range (len(groceries3))
for i in indexes:
        item= groceries3[i]
        print (f'{i}:{item}')"""
# user_input = input('enter the index you want to replace')
# print last_list [int(user_input)]
# print ('new value?')
# new_input = input('enter new value')
# groceries3.append = new_input
# print(groceries3)

# confim = f'you entered {int(size)}' #user input


#option1: 
# groceries1.extend(groceries2)

# #option2:
# groceries3 = groceries1 + groceries2

# - print the combined grocery list
# - prompt the user for the inddex of the item to replace
# - prompt the user for the new item
# - replace the item at that index with the new item
# - print the udpated combine list