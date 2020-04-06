
groceries = []

start_index_to_replace = int(input('enter first'))
end_index_to_replace = int(input('enter last'))

if start_index_to_replace == end_index_to_replace:
    new_item = input('new item')

    groceries[start_index_to_replace] = new_item
else:
    replacements = []
    while True:
        new_item = input ('What is the new item? ')
        if new_item == '':
            break
        replacements.append(new_item)
    print('----about to do weird thing-------')
    groceries[start_index_to_replace:end_index_to_replace] = replacements
    print('----just did weird thing---')
    print(groceries)

for i in indexes:
    item = groceries[i]
    print(f'{i}:{item}')