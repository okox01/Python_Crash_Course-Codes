from pathlib import Path  # Importing the Path class from pathlib module, which helps to handle file system paths

# Creating a Path object that represents the location of the 1 million digits of Pi text file
path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\1_million_of_Pi_digits.txt")

# Reading the content of the file into the 'contents' variable as a string
contents = path.read_text()

# Splitting the content of the file into a list of lines (list of strings)
lines = contents.splitlines()

# Initializing an empty string to store the concatenated digits of Pi without spaces
pi_string = ''

# Iterating through each line in the list of lines
for line in lines:
    pi_string += line.strip()  # Removing leading and trailing spaces from the line and adding it to pi_string

# Printing the first 52 characters of the concatenated string of Pi digits
print(pi_string[:52])

# Printing the total length of the concatenated string, which represents the number of characters
print(len(pi_string))
