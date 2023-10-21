# P-1. # A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the following sentence one hundred times: "I will never spam my friends again." Your program should number each of the sentences and it should make eight different random-looking typos.

import random

correct_sentences = 92
incorrect_sentences = 8
original_sentence = "I will never spam my friends again."
typos = ["1", "wil", "neverr", "span", "mine", "Friend", "gain"]

s = []

for _ in range(correct_sentences):
    s.append(original_sentence)

for _ in range(incorrect_sentences):
    words = original_sentence.split()
    word_index = random.randint(0, len(words) - 1)
    typo_index = random.randint(0, len(typos) - 1)
    words[word_index] = typos[typo_index]
    s.append(" ".join(words))

random.shuffle(s)

for i, s in enumerate(s, start=1):
    print(f"{i}. {s}")
