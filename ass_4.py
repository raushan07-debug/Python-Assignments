#Task 1


try:
    print("Reading file content:")
    with open("sample.txt", "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")



# Task 2


text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.\n")

# Take additional input 
append_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(append_text + "\n")

print("Data successfully appended.\n")

# Read and display 
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
