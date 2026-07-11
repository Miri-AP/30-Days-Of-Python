## 💻 Exercises: Day 10

### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print('for loop:', i)

while_loop_counter = 0
while while_loop_counter <= 10:
    print('while loop:', while_loop_counter)
    while_loop_counter += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print('for loop (countdown):', i)
while_loop_counter = 10
while while_loop_counter >= 0:
    print('while loop (countdown):', while_loop_counter)
    while_loop_counter -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
for i in range(1, 8):
    print('#' * i)
# 4. Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  # Move to the next line after each row

# 5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
while_loop_counter = 0
while while_loop_counter <= 10:
    print(f"{while_loop_counter} x {while_loop_counter} = {while_loop_counter * while_loop_counter}")
    while_loop_counter += 1

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
fruits = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for fruit in fruits:
    print('fruits:', fruit)
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print('even numbers:', i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print('odd numbers:', i)

### Exercises: Level 2

# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total += i
print('Sum of all numbers from 0 to 100:', total)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_of_evens = 0
sum_of_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_of_evens += i
    else:
        sum_of_odds += i
print(f"The sum of all evens is {sum_of_evens}. And the sum of all odds is {sum_of_odds}.")


### Exercises: Level 3
# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries import countries

for country in countries:
    if 'land' in country.lower():
        print('Country containing "land":', country)
# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print('Reversed fruit list:', reversed_fruits)

# 3. Go to the data folder and use the countries_data.py file.
from countries_data import countries_data


# What are the total number of languages in the data
total_languages = len(set(language for country in countries_data for language in country['languages']))
print('Total number of languages:', total_languages)

# Find the ten most spoken languages from the data
language_count = {}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

sorted_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 10 Most Spoken Languages")

for language, count in sorted_languages[:10]:
    print(language, "-", count)

# Find the 10 most populated countries in the world

most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]
print('Ten most populated countries:', [country['name'] for country in most_populated_countries])