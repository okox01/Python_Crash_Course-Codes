from pathlib import Path  # Importing the Path class from pathlib module, which helps to handle file system paths

path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\pi_value.txt")  # Creating a Path object that represents the location of the pi_value.txt file

contents = path.read_text()  # Reading the content of the pi_value.txt file into the 'contents' variable as a string

lines = contents.splitlines()  # Splitting the contents of the file into a list of lines (list of strings)

print(lines)  # Printing the list of lines to the console

pi_string = ''  # Initializing an empty string to store the concatenated text without leading spaces

for line in lines:  # Iterating through each line in the list of lines
    pi_string += line.lstrip()  # Adding the line to pi_string after removing any leading whitespace

print(pi_string)  # Printing the final concatenated string that contains all lines without leading spaces

print(len(pi_string))  # Printing the length of the concatenated string, which represents the number of characters in the string

# strip(): Removes characters from both the left and right ends of the string.
# lstrip(): Removes characters from the left (start) only.
# rstrip(): Removes characters from the right (end) only.