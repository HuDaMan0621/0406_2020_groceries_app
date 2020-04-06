
groceries = [] #list
item = input('enter an item') #asking for a user input
groceries.append(item) #assign the item to the list
print (groceries)
number_of_items = groceries

while number_of_items != (0): #infinite loop
    item = input('next item?')
    print (item)
    print ('press control C to exit')
print (groceries)
# #grpceries.append('Milk')