# we can import system package to provide console input to the program as follows
import sys


def addition(a,b):
    print(int(a)+int(b))

if __name__=="__main__":
    print(f"in {__name__} module")
    print(sys.argv)
    print(f"file name passed {sys.argv[0]}")
    print(f"first value passed {sys.argv[1]}")
    print(f"second value passed {sys.argv[2]}")
    addition(sys.argv[1], sys.argv[2])


