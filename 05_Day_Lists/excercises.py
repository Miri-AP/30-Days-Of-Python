# 1. Declare an empty list
empty_list = list()
print(len(empty_list)) # 0

# 2. Declare a list with more than 5 items
pets = ['dog', 'cat', 'fish', 'hamster', 'rabbit']
print(pets)

# 3. Find the length of your list
print(len(pets))

# 4. Get the first item, the middle item and the last item of the list
print(pets[0])  # First item
print(pets[len(pets)//2])  # Middle item
print(pets[-1])  # Last item

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
about_me = ['John Doe', 30, 1.48, False, '123 Main St']
print(about_me)
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print('number of companies:', len(it_companies))

# 9. Print the first, middle and last company
print('First company:', it_companies[0])
print('Middle company:', it_companies[len(it_companies)//2])
print('Last company:', it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[2] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Pinterest')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Tesla')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# 20. Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies)//2]
print('Middle company:', middle_company, 'of the list:', it_companies)

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)  # This should give: []

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack_copy. Then insert Python and SQL after Redux.
full_stack_copy = full_stack.copy()
redux_index = full_stack_copy.index('Redux')
full_stack_copy.insert(redux_index + 1, 'Python')
full_stack_copy.insert(redux_index + 2, 'SQL')
print(full_stack_copy)

## Exercises: Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
# Sort the list and find the min and max age
print('Sorted ages:', ages)
min_age = ages[0]
max_age = ages[-1]
print('Min age:', min_age)
print('Max age:', max_age)
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print('Ages with min and max added:', ages)
# Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages)//2] if len(ages) % 2 == 1 else (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
print('Median age:', median_age)
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print('Average age:', average_age)
# Find the range of the ages (max minus min)
range_ages = max_age - min_age
print('Range of ages:', range_ages)
# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print('Difference between min and average:', min_diff)
print('Difference between max and average:', max_diff)

# 1. Find the middle country(ies) in the countries list (from data/countries.py)
from countries import countries
middle_index = len(countries) // 2
if len(countries) % 2 == 1:
    middle_countries = [countries[middle_index]]
else:
    middle_countries = [countries[middle_index - 1], countries[middle_index]]
print('Middle country(ies):', middle_countries)
# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]
print('First half:', first_half, 'Length of first half:', len(first_half))
print('Second half:', second_half, 'Length of second half:', len(second_half))

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries_list
print('First country:', first_country)
print('Second country:', second_country)
print('Third country:', third_country)
print('Scandic countries:', scandic_countries)