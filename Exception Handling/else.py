# We can use else block with try-exception block
# else block is mostly used to give message and it will gets executed only if there is no error at try block
# else block is optional. We can use only one else block for each try block
# for example
file_obj = None

try:
    file_obj = open("test.txt","+w")
    file_obj.write("Hello")

except Exception as e:
    print(f"Error is {e}")


else:                                   # else gets executed only if there is no error at try block
    print("file updates successfully")


finally:
    file_obj.close()
    print("file is closed")


print("Program ends")
