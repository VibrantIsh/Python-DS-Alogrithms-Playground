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
print(unique_elements)  

# C-1.14 Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c', 'z'] but without having to type all 26 such character literally.
#Importing String Module.
import string
result = list(string.ascii_lowercase)
print(result)

#other way
alphas = list(chr(ord('a') +i) for i in range(26))
print(alphas)

# C-1.16 Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D.
lines = []
try:
    while True:
        line = input("Enter a line (or press Ctrl-D to finish): ")
        lines.append(line)
except EOFError:
    pass

lines.reverse()
for line in lines:
    print(line)

#C-1.18 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message: "Don't try buffer overflow attacks in Python!"
my_list = [1, 2, 3, 4, 5]

try:
    index = 10 
    value = 100
    my_list[index] = value
except IndexError:
    print("Don't try buffer overflow attacks in Python!")

#C-1.19 Write a short Python function that takes a strings, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return "Lets try Mike".
def remove_punctuation(sentence):
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    
    cleaned_sentence = ''.join(char for char in sentence if char not in punctuation)
    
    return cleaned_sentence

s = "Let's try, Mike."
result = remove_punctuation(s)
print(result)



