# workings out for seconds in year calculation:

HourSec = 60*60
DaySec = HourSec * 24
YearSecRes = DaySec * 365
LeapSecRes = DaySec * 366

# user input code:
DayYear = int(input("How many days are in this year? > "))

#adding commas was from my own reasearch/ addition after tutorial!

if DayYear == 366:
  print (format (LeapSecRes, ',d'),"seconds in a Leap Year!!")
elif DayYear == 365:
  print (format (YearSecRes, ',d'),"seconds in a Year!!") 
else:
  print ("Try again in earth years please!")
  
