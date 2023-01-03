import sys

names = ["atanda", "Bills", "David", "shola", "Kola"]
if "Bills" in names:
    print("Found")
    sys.exit(0)

print("Not Found")
sys.exit(1)