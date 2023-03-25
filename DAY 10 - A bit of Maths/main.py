Total = float(input("What was your total: "))
Percent = int(input("How Much would you like to Tip?: "))
People = int(input("How Many people are in your group? "))
tipTotal = Percent / 100 * Total
GrandTotal = Total + tipTotal
GrandTotal = round(GrandTotal,2)
print ("Your Grand Total is", GrandTotal)
split = GrandTotal / People
split = round(split,2)
print ("You Each owe: ", split)