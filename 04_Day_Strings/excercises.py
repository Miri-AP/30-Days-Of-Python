# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
result = word1 + ' ' + word2 + ' ' + word3 + ' '+ word4
print(result)  # 'Thirty Days Of Python'    
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word1 = 'Coding'
word2 = 'For'
word3 = 'All'
result = word1 + ' ' + word2 + ' ' + word3
print(result)  # 'Coding For All'
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4. Print the variable company using print().
print(company)
# 5. Print the length of the company string using len() method and print().
print(len(company))
# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:5])
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print(company.replace('Everyone', 'All'))
# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
social_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_media.split(','))
# 15. What is the character at index 0 in the string Coding For All.
print(company[0])
# 16. What is the last index of the string Coding For All.
print(len(company) - 1)
# 17. What character is at index 10 in "Coding For All" string.
print(company[10])
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print('Python For Everyone'.split()[0][0] + 'Python For Everyone'.split()[1][0] + 'Python For Everyone'.split()[2][0])
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print('Coding For All'.split()[0][0] + 'Coding For All'.split()[1][0] + 'Coding For All'.split()[2][0])
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find('because')
print(first_occurrence)
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_occurrence = sentence.rindex('because')
print(last_occurrence)
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[first_occurrence:last_occurrence + len('because')])
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[first_occurrence:last_occurrence + len('because')])
# 28. Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())
# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
challenge_isidentifier = '30DaysOfPython'
print(challenge_isidentifier.isidentifier())  # False
challenge_isidentifier2 = 'thirty_days_of_python'
print(challenge_isidentifier2.isidentifier())  # True
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))
# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')
# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name \t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
# 35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')
# 36. Make the following using string formatting methods:

# 8 + 6 = 14ß
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
number1 = 8
number2 = 6
print(f'{number1} + {number2} = {number1 + number2}')
print(f'{number1} - {number2} = {number1 - number2}')
print(f'{number1} * {number2} = {number1 * number2}')
print(f'{number1} / {number2} = {number1 / number2:.2f}')
print(f'{number1} % {number2} = {number1 % number2}')
print(f'{number1} // {number2} = {number1 // number2}')

formated_string = '%s ** %s' %(number1, number2)
print(f'{formated_string} = {number1 ** number2}')

