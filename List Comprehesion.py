#LIST COMPREHENSION AND FUNCTIONS

even_no_list = [] #initialize the list
#generate the list
for i in range(0,100+1,2):
    even_no_list.append(i)

#function to sum all list elements
def sum_even(number_list):
    sum = 0
    for i in number_list:
        sum+=i
    return sum

print(f'Even numbers between 1 and 100: \n{even_no_list}')
print(f'The sum of even numbers between 1 and 100: {sum_even(even_no_list)}')

#Code by Gerald Kumero