from pathlib import Path  # Importing the Path class from the pathlib module to work with file paths.

path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\sami.txt")  # Creating a Path object for the file location.

contents = path.read_text()  # Reading the contents of the file as a single string and storing it in the variable 'contents'.

lines = contents.splitlines()  # Splitting the string into a list of lines based on newline characters and storing it in 'lines'.

print(lines)  # Printing the list of lines. Each line from the file becomes an element in the list.
