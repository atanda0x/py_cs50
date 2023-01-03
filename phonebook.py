# people = {
#     "Atanda": "+234-903-864-806-8",
#     "Kolapo": "+234-807-142-064-8"
# }
# names = input("Name: ")
# if names in people:
#     #number = people[names]
#     print(f"Number: {people[names]}")

import csv

# file = open("phonebook.csv", "a")
name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])