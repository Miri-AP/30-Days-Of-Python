# 1. Create an empty tuple
empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Bella', 'Rosaline')
brothers = ('Emmet', 'Jasper', 'Edward')
print('Sisters:', sisters)
print('Brothers:', brothers)
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print('Siblings:', siblings)
# 4. How many siblings do you have?
num_siblings = len(siblings)
print('Number of siblings:', num_siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Esme', 'Carlisle')
print('Family members:', family_members)

## Level 2
# 1. Unpack siblings and parents from family_members
sisters = family_members[:3]
brothers = family_members[3:6]
parents = family_members[6:]
print('Sisters:', sisters)
print('Brothers:', brothers)
print('Parents:', parents)
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print('Food stuff tuple:', food_stuff_tp)
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list:', food_stuff_lt)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_lt[len(food_stuff_lt)//2]
print('Middle item(s):', middle_items)
# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print('First three items:', first_three)
print('Last three items:', last_three)
# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)