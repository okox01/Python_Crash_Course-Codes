# Importing the Path class from the pathlib module to work with file paths
from pathlib import Path

# Creating a Path object with the location of the file 'sami.txt' on your desktop
path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\sami.txt")

# Reading the content of the file 'sami.txt' and storing it in the variable 'contents'
contents = path.read_text()

# Printing the content of the file to the console
print(contents)


# Creating a Path object again for the same file 'sami.txt'
path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\sami.txt")

# Writing the text 'sami is a machine learning engineer.' to the file
# If the file doesn't exist, it will be created; if it exists, it will be overwritten.
path.write_text('sami is a machine learning engineer.')

# Reading the content of the file 'sami.txt' again after writing to it and printing the new content
print(path.read_text())


# Creating a Path object for the same file 'sami.txt'
path = Path(r"C:\Users\LENOVO\OneDrive\Desktop\sami.txt")

# Checking if the file exists at the specified path (returns True if it exists, False otherwise)
print(path.exists())


from pathlib import Path

path=Path(r'C:\Users\LENOVO\OneDrive\Desktop\sami.txt')
contents=path.read_text()
contents=contents.rstrip()
print(contents)

