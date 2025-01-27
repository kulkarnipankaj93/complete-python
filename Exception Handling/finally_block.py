# We can use finally block with try-except blocks
# Finally block has clean up code which will get executed in both cases whether we get any error or not
# Finally block is optional. we can use only one finally block for each try block
# Best example is when handling the file we can write close function in finally block
# for example
file_obj = None

try:
    file_obj = open("test.txt", "r")
    file_obj.write("new words")

except Exception as e:
    print(f"Error is {e}")

finally:
    file_obj.close()
    print("file is closed")

# finally:                       # There can only be one finally block for one try block
#     print("finally 2 block")


print("End of Program")
