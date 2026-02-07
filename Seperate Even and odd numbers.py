import numpy as np
#def seperate_even_and_odd_numbers its a function
def seperate_even_and_odd_numbers(numbers):
    numbers = np.array(numbers)
    even = numbers[numbers%2 == 0]
    odd = numbers[numbers%2!=0]
    return even,odd
#.spilt() is used to seperate the numbers by spaces entered by users
# map is used it takes two input 
numbers = list(map(int,input("Enter the numbers seperated by Spaces:").split()))

#To call the functions
even,odd = seperate_even_and_odd_numbers(numbers)
print("\nEven numbers:",even)
print("Odd numbers:",odd)