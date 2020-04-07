
#Class resume at 2 pm
# #to fill the grocery list:
# -prompt until they enter empty string

#show them the list
#- that is, print() it!

# Give them a chance to replace stuff in list
# -prompt for a subset of items to replace
# - if start and end same, replace 1
# if different, replace with a list 
# -(prompt until they enter empty string)




groceries = []

while True:
    
    item = input('What do you need from the store? ')
    if item in groceries:
        print (f'you already have {item}')
        break
    else: 
        groceries.append(item)    
#        try:
#     age=int(input('Enter your age: '))
# except:
#     print ('You have entered an invalid value.')
# else:
#     if age <= 21:
#         print('You are not allowed to enter, you are too young.')
#     else:
#         print('Welcome, you are old enough.')
    #temp_groceries = item #temp list to hold the new value 
    #if the item is duplicated, prompt user 
    #if item in temp_groceries: 
    #   print('already have')
    # check if user enters empty string
    if item is '':
        break
    
    #elif item in groceries:
        #print('you already have this item!')
        # try:
        #     pass
        # except expression as identifier:
        #     pass
        # else:
        #     pass
    indexes = range(len(groceries))
    for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')

# - prompt the user for the index of the item to replace
    question = input('Do you want to change an item? 1 for yes, 2 for no :')
    if question == '1':
            index_to_replace = int(input('What index to replace? '))
    
# - prompt the user for the new item
            new_item = input('What is the new item? ')

# - replace the item at that index with the new item
            groceries[index_to_replace] = new_item

    for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')
    # else:
    #         print(groceries)
    
# def checkfordup(groceries):
#     groceries_list = set()
#     for item in groceries_list:
#         if elem in groceries:
#             return True
#         else:
#             groceries.add(groceries)
# #     return False

# # def checkIfDuplicates_2(listOfElems):
# #     ''' Check if given list contains any duplicates '''    
# #     setOfElems = set()
# #     for elem in listOfElems:
# #         if elem in setOfElems:
# #             return True
# #         else:
# #             setOfElems.add(elem)         
# #     return False

# # listofelement = groceries
# # def checkIfDuplicates_1(groceries):
# #     ''' Check if given list contains any duplicates '''
# #     if len(groceries) == len(set(groceries)):
# #         return False
# #     else:
# #         return True
# #- print the updated combined list
#     # for i in indexes:
#     #     item = groceries[i]
#     # print(f'{i}: {item}')
        
#     # print(groceries)





# # while tem is True :
# #     item = input('What else do you need from the store? ')
# #     groceries1.append(item)
# #     print (groceries1)
# #     if item is None: #last item = nothing (empty)
# #         break
# #     print (groceries1)
    

# # groceries2 = []
# # while len(groceries2) < 3:
# #     item = input('What do you need from the store? ')
# #     groceries2.append(item)
# # ​
# # # combine the grocery lists
# # # Option 1: 
# # # groceries1.extend(groceries2)
# # ​
# # # Option 2:
# # groceries3 = groceries1 + groceries2
# # ​
# # # - print the combined grocery list
# # # print(groceries3)
# # indexes = range(len(groceries3))
# # for i in indexes:
# #     item = groceries3[i]
# #     print(f'{i}: {item}')
# # ​
# # - prompt the user for the index of the item to replace
# index_to_replace = int(input('What index to replace? '))
# ​
# # - prompt the user for the new item
# new_item = input('What is the new item? ')
# ​
# # - replace the item at that index with the new item
# groceries3[index_to_replace] = new_item
# ​
# # - print the updated combined list
# for i in indexes:
#     item = groceries3[i]
#     print(f'{i}: {item}')