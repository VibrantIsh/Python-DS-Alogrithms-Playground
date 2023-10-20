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

