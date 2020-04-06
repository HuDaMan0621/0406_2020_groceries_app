#write a function named 'repeat'
#it should accept 2 arguments:
#- a number
#- string
#it should print out the string however many times you specify.
#Example: Repeat(3, "good morning!")
# string = 'good morning'
# user_input = int(input('please enter a number '))
# while num <= user_input:
#     num + 1
#     print (num)

# change your function so that it returns instead of print()-ing
# need to study this 
# num = 0
# a_dog_says = 0
# num = int(input('Give me a number: '))
# while num <= a_dog_says:
#     print('woof')
#     num + 1
# print (a_dog_says)

#repeat(3, repeat(5, 'woof'))
def repeat(how_many_times, the_string):
    result = ''

    while how_many_times > 0:
        #do something
        #print(the_string)
        result += the_string
        how_many_times -= 1 #make my loop run x times

    return result
num = 5
a_dog_says = repeat(5, 'woof')
another_dog_says = repeat(3, a_dog_says)
repeat(5,'woof')
print (a_dog_says, another_dog_says)