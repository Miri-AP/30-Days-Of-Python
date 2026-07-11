## 💻 Exercises: Day 8

# 1. Create  an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3
print('dog:', dog)
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = dict() 
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 20
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'JavaScript']
student['country'] = 'USA'
student['city'] = 'New York'    
student['address'] = {'street': '123 Main St', 'zip_code': '10001'}
print('student:', student)
# 4. Get the length of the student dictionary
print('Length of student dictionary:', len(student))
# 5. Get the value of skills and check the data type, it should be a list
print('Skills:', student['skills'])
print('Type of skills:', type(student['skills']))
# 6. Modify the skills values by adding one or two skills
student['skills'].append('Java')
print('Updated skills:', student['skills'])
# 7. Get the dictionary keys as a list
print('Dictionary keys:', list(student.keys()))
# 8. Get the dictionary values as a list
print('Dictionary values:', list(student.values()))
# 9. Change the dictionary to a list of tuples using _items()_ method
print('Dictionary items:', list(student.items()))
# 10. Delete one of the items in the dictionary
del student['address']
print('Updated student dictionary:', student)
# 11. Delete one of the dictionaries
del student
print('Student dictionary deleted.')