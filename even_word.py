"""
P: Return the minimum number of letters removed that would make a string even
1. Take in a word
2. Make a dictionary to count the occurances of each letter
3. Declare a variable to store the amount of letters to be removed
4. If the the value of the letter is odd, add 1 to letters to be removed
"""

def even_word(word):
    counter = {};
    removed = 0;
    for letter in word:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in counter:
        if counter[letter] % 2 != 0:
            removed += 1

    return removed

