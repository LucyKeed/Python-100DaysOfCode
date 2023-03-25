#colour preset variables
default = "\033[0m"
green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
purp = "\033[35m"
cyan = "\033[36m"

#User input area
print (yellow, "*~*", purp, "EXAM GRADE CALCULATOR",yellow, "*~*",default)
test_name = input("What was your test called? > ")
max_score = float(input("What was the Maximum score? > "))
your_score = float(input("What was your score? > "))

#working out for score percentage
percent_decimal = float(your_score / max_score)
num_percent = round(percent_decimal, 2)
final_percent = round(float(your_score / max_score)*100, 2)

#printing the percentage result:
print("You got", final_percent,"%.")
print()

#printing the equivalent letter grade:
if num_percent == 100:
  print ("You got an",yellow,"A+.",default,"And you got all the questions right, thats incredible!🥳")
elif num_percent <= 99 and num_percent>= 90:
  print ("You got an",yellow,"A+.",default,"Excellent work!🤩")
elif num_percent <= 89 and num_percent >= 80:
  print ("You got an",cyan,"A.",default," Well Done!😍")
elif num_percent <= 79 and num_percent >= 70:
  print ("You got a", cyan,"B.",default, "Well Done!👏")
elif num_percent <= 69 and num_percent >= 60:
  print ("You got a",purp,"C.",default,"You did your best but make sure to revise more!👍")
elif num_percent <= 59 and num_percent >= 50:
  print ("You got a",red,"D.",default,"You might need to study more🙏")
elif num_percent <= 49 and num_percent >= 0:
  print ("You got a",red,"U.",default,"for ungraded... not great!👎😢")


print()
print ("""Grading Scale (Percentage): 
A+	90-100
A	80-89
B	70-79
C	60-69
D	50-59
U	under 50""")
