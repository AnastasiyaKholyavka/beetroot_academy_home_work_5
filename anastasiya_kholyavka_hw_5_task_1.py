'''
anastasiya_kholyavka
HW_5_task_1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets 
the user guess what number was generated. The result should be sent 
back to the user via a print statement.

'''

import random

computer = str((random.randint(1,10))) 
user = input('Введіть число від 1 до 10: ') 

print('computer = ' + computer)      
print('human = ' + user)     

if int(user) == int(computer):
    print('Ура, ви вгадали!')
else:
    print ('Не вгадали. Спробуйте ще!')