groceries = ['Milk', 'Bread', 'Beer']
completed = [True, False, False]

indexes = range(len(groceries))

for i in indexes:
    if completed[i]:
        print (f'{groceries[i]}:checked')
    else:
        print(f'{groceries[i]}:uncheck')