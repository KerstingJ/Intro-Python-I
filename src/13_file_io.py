"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
# get path up to current file
cwd = os.path.realpath(__file__)
path = cwd.replace("13_file_io.py", "foo.txt")

with open(path) as foo:
    for line in foo:
        print(line, end="")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
cwd = os.path.realpath(__file__)
path = cwd.replace("13_file_io.py", "bar.txt")

bar = open(path, mode="w")
for i in range(3):
    bar.write(f"This is line: {i}\n")

bar.close()
