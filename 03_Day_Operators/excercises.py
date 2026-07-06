# 1. Declare your age as integer variable
age = 29
# 2. Declare your height as a float variable
height = 1.75
# 3. Declare a variable that stores a complex number
complex_number = 3 + 4j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height_triangle
print("The area of the triangle is:", area)
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("The area of the rectangle is:", area_rectangle)
print("The perimeter of the rectangle is:", perimeter_rectangle)
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is:", area_circle)
print("The circumference of the circle is:", circumference)
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_1 = 2
y_intercept = -2
x_intercept = 1  # When y=0, 0 = 2x
print("X-intercept:", (x_intercept, 0))
print("Y-intercept:", (0, y_intercept))
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The slope between points (2, 2) and (6, 10) is:", slope)
print("The Euclidean distance between points (2, 2) and (6, 10) is:", f"{distance:.2f}")
# 10. Compare the slopes in tasks 8 and 9.
print("The slope in task 8 is:", slope_1)
print("The slope in task 9 is:", slope)
print("Are the slopes equal?", slope_1 == slope)
print("Is the slope in task 9 greater than the slope in task 8?", slope > slope_1)
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_values = [-10, -5, -3, 0, 1, 2, 3]
for x in x_values:
    value_y = (lambda x: x ** 2 + 6 * x + 9)
    if value_y(x) == 0:
        print(f"At x = {x}, y = 0")
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
print("Length of 'python':", length_python)
print("Length of 'dragon':", length_dragon)
print("Is the length of 'python' equal to the length of 'dragon'?", length_python == length_dragon)
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Is 'on' found in both 'python' and 'dragon'?", 'on' in 'python' and 'on' in 'dragon')
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("Is 'jargon' in the sentence?", 'jargon' in sentence)
# 15. There is no 'on' in both dragon and python
print("Is 'on' not found in both 'dragon' and 'python'?", 'on' not in 'dragon' and 'on' not in 'python')
# 16. Find the length of the text python and convert the value to float and convert it to string
length_python = len('python')
print("Length of 'python':", length_python)
print("Length of 'python' as float:", float(length_python))
print("Length of 'python' as string:", str(length_python))
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number to check if it is even or odd: "))
print(f"The number {number} is even." if number % 2 == 0 else f"The number {number} is odd.")
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Is the floor division of 7 by 3 equal to the int converted value of 2.7?", 7 // 3 == int(2.7))
# 19. Check if type of '10' is equal to type of 10
print("Is the type of '10' equal to the type of 10?", type('10') == type(10))
# 20. Check if int('9.8') is equal to 10
value = '9.8'
print("Is int('9.8') equal to 10?", int(float(value)) == 10)
# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter the number of hours worked: "))
rate_per_hour = float(input("Enter the rate per hour: "))
pay = hours * rate_per_hour
print(f"The pay of the person is: {pay}")
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years you want to calculate in seconds: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_in_a_year
print(f"The number of seconds in {years} years is a person can live: {total_seconds}")
# 23. Write a Python script that displays the following table
"""
 1 1 1 1 1
 2 1 2 4 8
 3 1 3 9 27
 4 1 4 16 64
 5 1 5 25 125
"""
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)