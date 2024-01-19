
# 1.Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result. Understand how variables store numerical values and perform basic arithmetic in Python.

#Declare tow variable

num1= 10
num2= 10

#calaculte value

sum= num1+num2

#print result
print("the sum of 10 & 10 is:", sum)


# 2.Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.

#create variable called message

message="Hello"

#Append the string
message +="World!"

#print update message

print("update message",message)

# 3. Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. Learn to use boolean variables for decision-making in Python.

#declare a boolean value
is_python_fun = True

if is_python_fun:
    print("Python is considered fun!")

else:
    print("Python may not be considered fun for everyone.")


# 4.Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list. Understand the basics of working with lists in Python.
    

fruit=["Apple", "Mango", "Banana"]

print("original fruit list is:", fruit)


#add a new fruit
update_fruit="orange"
fruit.append(update_fruit)

print("update fruit list is:",fruit)


# 5.Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values. Explore how to convert between different data types in Python.


#declare float value
price = 25.5

#float to int
int_price=int(price)

print("original price=",price)
print("convert price in integer:",int_price)


# 6.Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary. Learn how to work with dictionaries, a versatile data structure in Python.

info_student={
    "Name":"Hanzala",
    "Age":"19",
    "Grade" : "A1"
}

#print dict
print("Student Information:")
print("Name:",info_student["Name"])
print("Age", info_student["Age"])
print("Grade:",info_student["Grade"])


#7. Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement. Explore different ways to manipulate strings in Python.

string1= "Hi"
string2= "World"

combine_str= string1+""+string2

print("the combine string is:", combine_str, "and is the lenght is:", len(combine_str))

# 8. Create a tuple named days_of_week with the names of the days. Access and print the third day of the week. Understand the basics of working with tuples in Python

days_of_week=("Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday", "sunday")

the_third_day=days_of_week[2]

print("the third day of week is:", the_third_day)







