# P-1.29 Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list.

sentence_input = input("Enter your sentence here: ")
def functioning(word_list):
    words = word_list.split()
    word_dic = {}
    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic

passing = functioning(sentence_input)

for w, c in passing.items():
    if c > 1:
     print(f"{w} has: {c} count.")















