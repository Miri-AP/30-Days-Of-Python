## 💻 Exercises: Day 9

### Exercises: Level 1

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
'''Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 25  
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
else:
    print("We are the same age.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
number_a = float(input("Enter the first number (a): "))
number_b = float(input("Enter the second number (b): "))
if number_a > number_b:
    print(f"{number_a} is greater than {number_b}.")
elif number_a < number_b:
    print(f"{number_a} is smaller than {number_b}.")
else:
    print(f"{number_a} is equal to {number_b}.")

### Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:
'''
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''
score = float(input("Enter the student's score: "))
grades = {
    (90, 100): 'A',
    (80, 89): 'B',
    (70, 79): 'C',
    (60, 69): 'D',
    (0, 59): 'F'
}

for (min_score, max_score), grade in grades.items():
    if min_score <= score <= max_score:
        print(f"The student's grade is: {grade}")
        break
else:
    print("Invalid score. Please enter a score between 0 and 100.")

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
season_months = {
    'Autumn': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February'],
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August']
}
month = input("Enter the month: ").capitalize()
for season, months in season_months.items():
    if month in months:
        print(f"The season is {season}.")
        break
else:
    print("Invalid month. Please enter a valid month name.")
# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Enter the name of a fruit: ").lower()
if fruit_input in fruits:
    print(f"{fruit_input} is already in the list.")
else:
    fruits.append(fruit_input)
    print(f"{fruit_input} has been added to the list.")

### Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person: 
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"The middle skill is: {skills[middle_index]}")
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_python_skill = 'Python' in person['skills']
    print(f"Does the person have Python skill? {has_python_skill}")
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, etc, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) == {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif 'React' in skills and ('Node' in skills and 'MongoDB' in skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')
# * If the person is married and if he lives in Finland, print the information in the following format:
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


