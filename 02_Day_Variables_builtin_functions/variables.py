print('Day 2: 30 Days of python programming')
# Variables in Python

first_name = 'John'
last_name = 'Tucker'
full_name = first_name + ' ' + last_name
country = 'Finland'
city = 'Helsinki'
age = 35
year = 2026
is_married = False
is_light_on = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'John',
    'lastname': 'Tucker',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, year, is_married, is_light_on = 'John', 'Tucker', 'Helsink', 35, 2026, False, True

print(first_name, last_name, country, age, year, is_married, is_light_on)
print('First name:', first_name, len(first_name))
print('compare first and last name: ', len(first_name), len(last_name))

num_1, num_2 = 5, 4
num_total = num_1 + num_2
print('Total: ', num_total)
num_diff = num_1 - num_2
print('Difference: ', num_diff)
num_multiply = num_1 * num_2
print('Multiplication: ', num_multiply)
num_division = num_1 / num_2
print('Division: ', num_division)
num_power = num_1 ** num_2
print('Power: ', num_power)
floor_division = num_1 // num_2
print('Floor division: ', floor_division)

circle_radius = 30
area_of_circle = 3.14 * circle_radius ** 2
print('Area of circle: ', area_of_circle)
circum_of_circle = 2 * 3.14 * circle_radius
print('Circumference of circle: ', circum_of_circle)

input_radius = input('Enter radius: ')
area_of_circle = 3.14 * int(input_radius) ** 2
print('Area of circle: ', area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter your first name: ') 
print('First name: ', first_name)
last_name = input('Enter your last name: ')
print('Last name: ', last_name)
country = input('Enter your country: ')
print('Country: ', country)
age = input('Enter your age: ')
print('Age: ', age)
