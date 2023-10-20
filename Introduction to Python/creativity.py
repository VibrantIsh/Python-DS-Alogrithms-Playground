#C-1.10 Write a prudocode description of a function that reverses a list of integers, so that the numbers are listed in the opposite onder than they were before, and compare this method.
function reverseList(originalList):
   create an empty list called reversedList
   for each item in the original list starting from the end:
      append this item to reversedList
   return reversedList

#C-1.11 Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of consecutive numbers in the sequence whose product is even.
def is_even_product(lst):
    for i in range(len(lst) -1):
        current_num = lst[i]
        next_num = lst [i + 1]
        if (current_num * next_num ) % 2 == 0:
            return True
    else:
        return False

# C-1.12 Write a Python function that takes a sequence of numbers and returns the count of unique numbers (that is, numbers that are distinct)
def count_unique_elements(lst):
    unique_elements = []
    for i in lst:
        if i not in unique_elements:
            unique_elements.append(i)
    return len(unique_elements)

my_list = [1, 2, 4, 7, 8, 9, 0, 6, 7, 5, 3, 1]
result = count_unique_elements(my_list)
print(result)

# using set() function.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print(unique_elements)  # Output: {1, 2, 3, 4, 5}
