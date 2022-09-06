'''
anastasiya_kholyavka
HW_5_task_2

Write a program that takes your name as input, and then your age 
as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   

'''
name = input('Type your name: ')
age = int(input('Type your age: '))+1
#age = age + 1

print('Hello,' + ' ' + name + ',' + ' ' + 'on your next birthday you’ll be' + ' ' + str(age))