# name = input('What is your name? ')
# print('Hello ' + name)

# name = 'Jamila'
# age = 18
# pi = 3.14
# cars = ['bmw', 'mercedes', 'range rover']

# print(name)
# print(age)
# print(pi)
# print(cars)

# first_name = 'Jamila'
# surname = 'Smith'
# full_name = first_name + ' ' + surname

# print(full_name)
# print(len(first_name))
# print(len(surname))

# first_name = 'jamila'
# surname = 'Smith'
# full_name = first_name.capitalize() + ' ' + surname

# print(full_name)
# print(len(first_name))
# print(len(surname))
# print(full_name.endswith('Smith'))

# addition = 10 + 5
# subtraction = 10 - 5
# multiplication = 10 * 5
# division = 10 / 5
# mod = 10 % 5

# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(mod)

# print(10 <= 10)
# print(0 == 1)
# print(18 > 5)
# print('Jamila'.endswith('s'))
# print('Jamila'.endswith('a'))

# is_adult = True
# is_teenager = False

# is_adult = True

# if is_adult:
#     print("is adult")

# is_adult = False

# if is_adult:
#     print("is adult")

# is_adult = False
# age = 18
# age = 17

# if is_adult:
#     print("is adult")

# if age >= 18:
#     print('adult')
# else:
#     print('not an adult')

# car = 'bmw'
# cars = ['bmw', 'tesla', 'mercedes', 'toyota']
# print(len(cars))
# print(cars)
# print(cars[0])
# print(cars[1])
# print(cars[2])
# print(cars[3])

# cars = ['bmw', 'tesla', 'mercedes', 'toyota', 'honda']

# for car in cars:
#     print(car)

# for car in cars:
#     print(car.capitalize())

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.capitalize())

# number = 0

# while number <= 10:
#     print(number)
#     number = number + 1

# while number <= 10:
#     print(number)
#     number = number + 1
# else:
#     print('while loop ended and value of number is ' + str(number))

# age = 18
# age2 = 17

# def check_age():
#     print('check age function was invoked')

# if age < 18:
#     print('ooops not an adult')
# else:
#     print('hooray I am an adult')

# if age2 < 18:
#     print('ooops not an adult')
# else:
#     print('hooray I am an adult')

# def check_age():
#     if age < 18:
#         print('ooops not an adult')
#     else:
#         print('hooray I am an adult')

# check_age()

# def check_age(age):
#     if age < 18:
#         print('ooops not an adult')
#     else:
#         print('hooray I am an adult')

# check_age(age)
# check_age(age2)
# check_age(18)
# check_age(17)
# check_age(999)

# 'hello'.upper()
# 'hello'.capitalize()
# 'hello'.startswith('')
# 'hello'.endswith('')

# print('hello'.endswith('O'))
# print('hello'.endswith('o'))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# john = Person('John', 22)
# mariam = Person('Mariam', 18)

# print(john.name + ' ' + str(john.age))
# print(mariam.name + ' ' + str(mariam.age))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         print(self.name + ' is walking...')

#     def speak(self):
#         print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old')

# john = Person('John', 22)
# mariam = Person('Mariam', 18)

# print(john.name + ' ' + str(john.age))
# john.speak()
# john.walk()

# print('---------------------------------------------')

# print(mariam.name + ' ' + str(mariam.age))
# mariam.speak()
# mariam.walk()

# from docx import Document
# from docx.shared import Inches
# import pyttsx3

# def speak(text):
#     pyttsx3.speak(text)

# document = Document()

# # profile picture
# document.add_picture(
#     'me.jpg',
#     width=Inches(2.0)
# )

# # name phone number and email details
# name = input('What is your name? ')
# speak('Hello ' + name + ' how are you today? ')
# speak('What is your phone number? ')
# phone_number = input('What is your phone number? ')
# email = input('What is your email? ')

# document.add_paragraph(
#     name + ' | ' + phone_number + ' | ' + email)

# # about me
# document.add_heading('About Me')
# about_me = input('Tell me about yourself? ')
# document.add_paragraph(about_me)

# # work experience
# document.add_heading('Work Experience')
# p = document.add_paragraph()

# company = input('Enter company ')
# from_date = input('From Date ')
# to_date = input('To Date ')

# p.add_run(company + ' ').bold = True
# p.add_run(from_date + '-' + to_date + '\n').italic = True

# experience_details = input(
#     'Describe your experience at ' + company + ' ')
# p.add_run(experience_details)

# #more experiences
# while True:
#     has_more_experiences = input(
#         'Do you have more experiences? Yes or No ')
#     if has_more_experiences.lower() == 'yes':
#         p = document.add_paragraph()

#         company = input('Enter company ')
#         from_date = input('From Date ')
#         to_date = input('To Date ')

#         p.add_run(company + ' ').bold = True
#         p.add_run(from_date + '-' + to_date + '\n').italic = True

#         experience_details = input(
#             'Describe your experience at ' + company + ' ')
#         p.add_run(experience_details)
#     else:
#         break

# #skills
# document.add_heading('Skills')
# skill = input('Enter skill ')
# p = document.add_paragraph(skill)
# p.style = 'List Bullet'

# while True:
#     has_more_skills = input('Do you have more skills? Yes or No ')
#     if has_more_skills.lower() == 'yes':
#         skill = input('Enter skill ')
#         p = document.add_paragraph(skill)
#         p.style = 'List Bullet'
#     else:
#         break

# #footer
# section = document.sections[0]
# footer = section.footer
# p = footer.paragraphs[0]
# p.text = 'CV generated using Amigoscode and Intuit QuickBooks course project'

# document.save('cv.docx')
