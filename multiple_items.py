# groceries = ["milk ", "Bread", 'Beer', 'more Beer']
# print (groceries[0:2]) #[0:2] slice function
# #["Milk", "Bread"]


groceries = ['Beer','2','3'] 
groceries2 = groceries[:]
groceries2.append('Cabbage')

print(groceries)



#check is beer on the list
'Beer' in groceries
if 'Beer' not in groceries:
    print('beer not in groceries')
else:
    print('yep it is in there')
