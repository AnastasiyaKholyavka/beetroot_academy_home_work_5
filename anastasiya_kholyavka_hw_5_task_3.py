'''
anastasiya_kholyavka
HW_5_task_3

Words combination

Create a program that reads an input string and then creates and prints 
5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, so it should print 5 
random strings(words) that combine characters 

'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)

'''
import random

word = input('Print a word: ')

new_word = random.choices(word, k = 5)

i = 0
while i < 5:
    print(''.join(new_word)) 
    i = i + 1

# Всі нові констукції однакові
