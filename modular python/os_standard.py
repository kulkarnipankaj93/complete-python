# following are different methods we can use by importing standard module os
import os

# to get current working directory
dire = os.getcwd()
print(dire)

# to list down all files present in current working directory
files = os.listdir()
print(files)

# to make single directory
# os.mkdir("new folder")         # if same name folder is already present we get error

# change current working directory
os.chdir("new folder")
print(os.getcwd())

# to make multiple directories
# os.makedirs("f1\\f2\\f3")         # if same folder names are already present we get error

os.chdir("f1\\f2\\f3")
print(os.getcwd())

file1 = open("trial.txt","+w")
file1.write("sample text")
file1.close()
