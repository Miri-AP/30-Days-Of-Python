# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1

# 1. Find the length of the set it_companies
print('Length of it_companies:', len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('It companies after adding Twitter:', it_companies)
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'SpaceX'])
print('It companies after adding Tesla and SpaceX:', it_companies)
# 4. Remove one of the companies from the set it_companies
it_companies.discard('Facebook')
print('It companies after removing Facebook:', it_companies)
# 5. What is the difference between remove and discard
# if an item does not exist in the set, remove() will give an Error (keyError), while discard() won't.

### Exercises: Level 2

# 1. Join A and B
joined_set = A.union(B)
print('Joined set A and B:', joined_set)

# 2. Find A intersection B
print('Intersection of A and B:', A.intersection(B))
# 3. Is A subset of B
print('Is A subset of B:', A.issubset(B))
# 4. Are A and B disjoint sets
print('Are A and B disjoint sets:', A.isdisjoint(B))
# 5. Join A with B and B with A
print('Join A with B:', A.union(B))
print('Join B with A:', B.union(A))
# 6. What is the symmetric difference between A and B
print('Symmetric difference of A and B:', A.symmetric_difference(B))
# 7. Delete the sets completely
del A
del B

### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print('Length of the list:', len(age))
print('Length of the set:', len(age_set))
# 2. Explain the difference between the following data types: string, list, tuple and set
# a string is a sequence of characters
# a list is an ordered collection of items that can be changed, Allows duplicate members
# a tuple is an ordered collection of items that cannot be changed (unmodifiable). Allows duplicate members.
# a set is an unordered collection of unique items (un-indexed and unmodifiable). Does not allow duplicate members.

# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print('Number of unique words:', len(unique_words), '\nUnique words:', unique_words)