import sys

numbers =  [2, 1, 4, 6, 8, 9, 0]

if 0 in numbers:
    print("Found")
    sys.exit(0)
print("Not found")
sys.exit(1)