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
'''
import random

word = input('Please, type a word: ')

# спроба 1

print(random.choices(word)) # Треба, щоб це повторилося 5 разів, без дублювання прінт
print(random.choices(word)) 
print(random.choices(word)) 
print(random.choices(word)) 
print(random.choices(word)) 

print(random.shuffle(list(word))) # Як зробити з кожної літери окремий елемент списку, а не рядка, щоб перемішати їх?
'''

# спроба 2

import random

word = input('Please, type a word: ')

random_letter_1, random_letter_2, random_letter_3, random_letter_4, random_letter_5 = (random.choices(word)), (random.choices(word)), (random.choices(word)), (random.choices(word)), (random.choices(word))


new_list = [random_letter_1, random_letter_2, random_letter_3, random_letter_4, random_letter_5]

print(new_list)
print(random.shuffle(new_list)) # Це не працює 


