from pathlib import Path  # Importing the Path class from the pathlib module, which allows easy handling of file system paths

# Creating a Path object to represent the file containing the first million digits of Pi
path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\1_million_of_Pi_digits.txt")

# Reading the entire contents of the file as a string and storing it in the 'contents' variable
contents = path.read_text()

# Splitting the file contents into a list of lines (each line will be a string in the list)
lines = contents.splitlines()

# Initializing an empty string to store the concatenated digits of Pi without spaces
pi_string = ''

# Iterating through each line in the list of lines from the Pi file
for line in lines:
    pi_string += line.strip()  # Removing leading/trailing whitespace from the line and appending it to the pi_string

# Prompting the user to input their birthday in the format ddmmyy (day-month-year)
dob = input("Enter your birthday (ddmmyy): ")

# Checking if the entered birthday (dob) is found within the string pi_string (the concatenated digits of Pi)
if dob in pi_string:
    print("Your birthday is in Pi!")  # If the birthday is found, print this message
else:
    print("Your birthday is not in Pi.")  # If the birthday is not found, print this message

