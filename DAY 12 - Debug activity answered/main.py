#Fixing code! 

print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
print()
#ANSWER ONE
ans1 = input("What language are we writing in? > ")
print()
if ans1 == "python": 
  print("Correct")
else:
  print("Nope🙈")
#ANSWER TWO
print()
ans2 = int(input("Which lesson number is this? > "))
print()
if (ans2 > 12):
  print("We're not quite that far yet")
elif (ans2 == 12):
  print("That's right!")
else:
  print("We've gone well past that!")