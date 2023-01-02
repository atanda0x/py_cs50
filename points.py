points = int(input("How many point did you lose: "))

if points > 2:
    print("You lost more points than me")
elif points < 2:
    print("You lost fewer points than me")
else:
    print("You lost same number of points as me")
