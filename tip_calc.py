bill = float(input("how much was the bill ? \n"))

participants = int(input("how many of you took part to the meal? \n"))

tip = int(input("how much percentage do you want to leave as tip?  \n"))

print("each of you should pay " + str(round((bill + (bill/100*tip)) /participants,3 )))
