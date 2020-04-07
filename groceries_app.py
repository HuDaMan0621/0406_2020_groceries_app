
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
import time
groceries = ['Milk', 'Chicken', 'Eggs']

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''
sub_menu = '''
1. Print List
2. Delete an Item
3. Delete multiple Items
4. Return to main menu

'''

while True:

#     num = 0
# while True:
#         try:
#             num = int(input('Give me a number: '))
#             break
#         except ValueError:
#             print('please try again.')
# print(f'you entered {num}')
        try:
            menu_choice = int(input(main_menu))

            if menu_choice == 5:
                print ('Thank you for using the grocery list app!')
                break
    
            if menu_choice == 1: #print list
                print (groceries)

            if menu_choice == 2: #add items
                while True:
                    
                    item = input('What item would you like to add to the Shopping List?: \n Are you Finishe? Type End to end: ')
                    if item == ('End'):
                        break
                    groceries.append(item)
                    indexes = range(len(groceries))
                    for i in indexes:
                        item = groceries[i]
                        print(f'{i}: {item}')
                    print(groceries)
                
            if menu_choice == 3: #Edit items
                indexes = range(len(groceries))
                for i in indexes:
                    item = groceries[i]
                    print (f'{i} : {item}')
                    #time.sleep(1.3)
                #print(f'{groceries}testing here')
                
                index_to_replace = int(input('Enter index here'))
                        # # - prompt the user for the new item
                new_item = input('What is the new item? ')
                        #  - replace the item at that index with the new item
                groceries[index_to_replace] = new_item
                            
                        # indexes = range(len(groceries))
                        # for i in indexes:
                        #     item = groceries[i]
                        #     print(f'{i}: {item}\n')
            
            if menu_choice == 4: #remove items
                while True:
                    sub_menu_choice = int(input(sub_menu))
                    indexes = range(len(groceries))#len grabs the length of the list in groceries 
                        #(indexes = 0, 1 ,2 count )
                    for i in indexes: #i becomes the variable, i = index, each spot in groceries
                        #print (i) #always print the information 
                        item = groceries[i] #each item in groceries[i]
                        print (f'{i} : {item}') #replace {varibles }
                        #time.sleep(1) make it print slower 
                
                    index_to_remove = int(input('what item do you want to remove? '))
                    groceries.pop(index_to_remove)
                    print(groceries)
                    print('end')
        except ValueError:
                print('Please select from Menu')
        except :
                print('cannot pop from empty list')
#        try:
#     age=int(input('Enter your age: '))
# except:
#     print ('You have entered an invalid value.')
# else:
#     if age <= 21:
#         print('You are not allowed to enter, you are too young.')
#     else:
#         print('Welcome, you are old enough.')
#    indexes = range(len(groceries))
#     for i in indexes:
#             item = groceries[i]
#             print(f'{i}: {item}')

# # - prompt the user for the index of the item to replace
#     question = input('Do you want to change an item? 1 for yes, 2 for no :')
#     if question == '1':
#             index_to_replace = int(input('What index to replace? '))
    
# # - prompt the user for the new item
#             new_item = input('What is the new item? ')

# # - replace the item at that index with the new item
#             groceries[index_to_replace] = new_item

#     for i in indexes:
#             item = groceries[i]
#             print(f'{i}: {item}')
#     else:
#             print(groceries)
    









# # def checkfordup(groceries):
# #     groceries_list = set()
# #     for item in groceries_list:
# #         if elem in groceries:
# #             return True
# #         else:
# #             groceries.add(groceries)
# # #     return False

# # # def checkIfDuplicates_2(listOfElems):
# # #     ''' Check if given list contains any duplicates '''    
# # #     setOfElems = set()
# # #     for elem in listOfElems:
# # #         if elem in setOfElems:
# # #             return True
# # #         else:
# # #             setOfElems.add(elem)         
# # #     return False

# # # listofelement = groceries
# # # def checkIfDuplicates_1(groceries):
# # #     ''' Check if given list contains any duplicates '''
# # #     if len(groceries) == len(set(groceries)):
# # #         return False
# # #     else:
# # #         return True
# # #- print the updated combined list
# #     # for i in indexes:
# #     #     item = groceries[i]
# #     # print(f'{i}: {item}')
        
# #     # print(groceries)





# # # while tem is True :
# # #     item = input('What else do you need from the store? ')
# # #     groceries1.append(item)
# # #     print (groceries1)
# # #     if item is None: #last item = nothing (empty)
# # #         break
# # #     print (groceries1)
    

# # # groceries2 = []
# # # while len(groceries2) < 3:
# # #     item = input('What do you need from the store? ')
# # #     groceries2.append(item)
# # # ​
# # # # combine the grocery lists
# # # # Option 1: 
# # # # groceries1.extend(groceries2)
# # # ​
# # # # Option 2:
# # # groceries3 = groceries1 + groceries2
# # # ​
# # # # - print the combined grocery list
# # # # print(groceries3)
# # # indexes = range(len(groceries3))
# # # for i in indexes:
# # #     item = groceries3[i]
# # #     print(f'{i}: {item}')
# # # ​
# # # - prompt the user for the index of the item to replace
# # index_to_replace = int(input('What index to replace? '))
# # ​
# # # - prompt the user for the new item
# # new_item = input('What is the new item? ')
# # ​
# # # - replace the item at that index with the new item
# # groceries3[index_to_replace] = new_item
# # ​
# # # - print the updated combined list
# # for i in indexes:
# #     item = groceries3[i]
# #     print(f'{i}: {item}')