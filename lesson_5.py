# my_list = [1,3,4,5,7]
# print(my_list)
# extension = [[7,8,10,9,11]]
# my_list.insert(2, 4)

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# sum = 1

# for element in my_list:
#     sum *= element 

# print(sum)

# max = 0

# name = input('enter your name')
# surname = input('Enter your sourname: ')

# a = 0
# b = 0
# for element in name:
#     a += 1 
# for element in surname:
#     b += 1 
# print(f'name {a}, surname {b})





# my_list = ['північна америка','південна америка']
# right = ['євразія','африка','австралія']
# my_list.extend(right)
# for element in my_list:
#     if type(element) == list:
#         element.sort()
# my_list.sort()
# print(my_list)

# # 


# # s = str(15)
# # print(type(s))

# # s = str([12,15])
# # print(type(s))

# # s = 'ABCDEFGHI'
# # n = int(input('ur char:'))

# # if n > len(s):
# #     print('wrong input!')

# # else:
# #     new_string = s[n:]

# # print(new_string)

# # print('pi: {:0,6}')

# # # 2 
# # string = 'abcd1234efg567'
# # newstring = ''.join([i for i in string if not i.isdigit()])
# # print(newstring)


# # # 1 
# # s = str(input("напишіть ваше прізвище: "))
# # h = str(input("символи,які потрібні знайти:"))
# # count = 0;
# # for c in s:
# #     if c==h:
# #         count = count+1

# # print("count = ", count)

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # en = numbers[2:-1:3]
# # print(en)

# # pip = 'Ivan Ivanov'
# # delimiter = ' '
# # space = pip.find(delimiter)

# # name = pip[0:space]
# # last_name = pip[space+1:]

# # print(name,last_name)
# # phones = ['+38(067) 999-99-99', '+38(066) 999-99-99','+38(067) 888-88-88', '+38(068) 777-77-77']
# # kiivstar = ['+067','+098','+068']
# # count = 0 
# # for element in phones:
# #     operator_code = element[4:7]
# #     if operator_code in kiivstar:
# #         count += 1 

# # print(count)

# monthes = {
#     1:  'січень',
#     2:  'лютий',
#     3:  'березень',
#     4:  'квітень',
#     5:  'травень',
#     6:  'червень',
#     7:  'липень',
#     8:  'серпень',
#     9:  'вересень',
#     10: 'жовтень',
#     11: 'листтопад',
#     12: 'грудень'
# 

# currencies = {
#     'usd': 36.5,
#     'eur': 39.4,
#     'gbp': 43.8,
# }

# currencies['usd'] = {39}
# currencies['eur'] = {41}
# currencies['gbp'] = {44}

# currency = input('Enter the currency you wold like to exchange:')
# amount = float(input('how much money you would to exchange?'))

# print(currencies.values())

# if currencies not in currencies.keys():
#     print('we don\'t support such curency')
# else:
#     amount = float(input('how much money do u want to exchamge'))
#     result = round(amount*currencies[currency], 2)
#     print('here is your {"39","41","44"} uah'.format(result)) 

# user = {
#     "name": "Bill",
#     "surname": "Bosh",
#     "age": 22
# }
# for ages in user:
# print(ages)

# def say_hello():
#     a=5
#     b=7
#     print(a+b)

# say_hello()

# def pyramid():
#     for i in range(100):
#         i += 1
#         print('*' * i)

# pyramid()

# def suma(a,b):
#     return a + b 

# def substraction(a,b):
#     return a - b 

# def power(a,b):
#     return a ** b

# def multiplay(a,b):
#     return a * b

# def calculation(opperand_A,oppernd_B,operator):
#     if operator not in ['+','-','*','^']
#         print('invalid operator')
#     else:
#         match operator:
#             case '+':
#                 result = suma(opperand_A,oppernd_B)
#             case '-':
#                 result = substraction(opperand_A,oppernd_B)
#             case '*':
#                 result = multiplay(opperand_A,oppernd_B)
#             case '^':
#                 result = power(opperand_A,oppernd_B)

#         print(opperand_A,operator,oppernd_B,'=',result)

# a = float(input('enter the first opperand'))
# b = float(input('enter second opperand'))

# print('avalibie operators = [])

# from collections import Counter

# s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
# s = s.replace(" ", "")
# counter = Counter(s)

# for c, count in counter.most_common(1):
#     print(c)

# surname = input('enter your name: ')
# counter = dict()

# for char in surname:
#     counter[char] = surname.count(char)

# the_most_comman = ''

# most_common = max(list(counter.items()), key=lamda x:[1])
# print(most_common[0])

# string = input() + ' '
# space = string.find(' ')
# word = string[:space]
# new_string = string[space+1:]

# for i in range(string.count(' ')):
#     space = new_string.find(' ')
#     if len(new_string[:space]) >= len(word):
#         word = new_string[:space]
#     new_string = new_string[space+1:] 

# print(f'the longest word is {word}')  

# grades = {
#     "Dmytro": 2,
#     "Anna": 5,
#     "Mykyta": 3,
#     "Andrii": 4
# }

# good_grades = dict()

# for student_name, grade in grades.items():
#     if grade >= 4:
#         good_grades[student_name] = grade

# print(good_grades)

# #1
# sum = 0 
# for number in range(1 , 100+1):
#     if number % 2 != 0:
#         print(number)
#         sum += number

# print('sum:',sum,end=' ')

# #2
# string = input('enter your string: ')
# first_char = string[0]
# count = 0
# for char in string:
#     if char == first_char:
#         count += 1 

# print(f'Amount of the first letter {first_char} is {count}')

# # 1
# # Створимо список материків західної півкулі
# west_continents = ['Північна Америка', 'Південна Америка']

# # Доповнимо список материками східної півкулі 
# east_continents = ['Євразія','Африка', 'Австралія']
# all_continents = west_continents + east_continents

# # Сортування та виведення на екран
# all_continents.sort()
# print(all_continents)

# #2 
# #список студентів
# students = [    ['Андрій', 'Ковальчук'],
#     ['Олена', 'Петренко'],
#     ['Іван', 'Довгий'],
#     ['Андрій', 'Сірий'],
#     ['Оксана', 'Гончаренко'],
#     ['Олександр', 'Кравченко'],
#     ['Андрій', 'Гончар'],
#     ['Юлія', 'Іванова'],
# ]
# # рахуємо кількість слів "андрій" через функцію
# count = 0
# for student in students:
#     if student[0] == 'Андрій':
#         count += 1

# print(f"Кількість людей з ім'ям 'Андрій': {count}")

# string = input() + ' '

# string = input().strip() + ' '
# string += ' '
# space = string.find(' ')

# word = string[:space]
# new_string = string[space+1:]

# print(string.count(' '))
# for i in range(string.count(' ')):
#     space = new_string.find(' ')
#     if len(new_string[:space]) >= len(word):
#         word = new_string[:space]
#     new_string = new_string[space+1:] 

# print(f'the longest word is {word}')  

# def function(list):
#     a = len(list)
#     b = sum(list)
#     return b/a

# print(function([1,3,4,5,6,2,3]))

# my_dict = {
#     'яблуко': 1,
#     'банан': 2,
#     'апельсин': 3
# }
# def get_value(dct, key):
#     if key in dct:
#         return dct[key]
#     else:
#         return None
# print(get_value(my_dict, 'банан'))
# forecast = {
#     "kiyiv": 25,
#     "chercasy": 27,
#     "odessa": 30,
#     "donetsk": 26,
# }

# total_temp = 0
# count = len(forecast)

# for temp in forecast.values():
#     total_temp += temp

# print(f'avarage temperatures on city = {total_temp/count}')

text = 'The quick brown fox jumps over the lazy dog'

chars_count = dict()
for char in text:
    if char !=' ':
        if char not in chars_count:
            chars_count[char] = text.count(char)

print(chars_count)
