import csv

counter = 0

title = input("Title: ").strip().upper()
with open("Favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        if row["title"].strip().upper() == title:
            counter += 1
        