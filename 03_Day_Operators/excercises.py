

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
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# 15. There is no 'on' in both dragon and python
# 16. Find the length of the text python and convert the value to float and convert it to string
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

