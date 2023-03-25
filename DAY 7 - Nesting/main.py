print("Welcome to The L House!")
entrance = input("Which way do you want to go? Left, right or upstairs: ")
if entrance == "left":
  print ("youre in the living room!")
  downleft = input("would you like to go into the kitchen? Y or N: ")
  if downleft == "Y":
    print("lets have a cuppa!")
  elif downleft == "N":
    print ("lets watch some TV!")
elif entrance == "right":
  print ("this is our office!")
elif entrance == "upstairs":
  print ("welcome to the landing")
else:
  print ("ok, we can go there later")