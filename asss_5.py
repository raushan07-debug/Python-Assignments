#Task 1
# Create a dictionary of student marks


student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Ask user to enter student name
name = input("Enter the student's name: ")

# Check and display result
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")


#Task 2
# Create a list of numbers from 1 to 10


numbers = list(range(1, 11))

# Extract the first five elements
first_five = numbers[:5]

# Reverse the extracted elements
reversed_list = first_five[::-1]

# Print the results
print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)
