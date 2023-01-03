import csv

#titles = [] 

titles = dict()
with open("Favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        title = row["title"].strip().upper()
        # titles.add(title)
        if not title in titles:
            titles[title] = 0
        titles[title] += 1

for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])