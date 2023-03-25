print("Hello there, 😄 i'm your friendly neightbourhoor PC! Nice to meet you! Lets get to know each other!")
print()
name = input("What is your name? > ")
print ("Hi", name)
place = input("So,where do you live? > ")
if place == "bristol" or place == "Bristol":
  print ("Alright my luvverr!")
  brisfav = input ("What is your favourite place there? > ")
  if brisfav == "harbour":
    print ("i love the habourside too!")
  elif brisfav == "suspension bridge":
    print ("ahh a marvellous feet of engineering!")
  else:
    print ("ooh wow, ive not been there before!")
elif place == "weston" or place == "weston-super-mare":
  print ("Oh we do like to be beside the seaside!")
  wesfav = input ("What is your favourite place there? > ")
  if wesfav == "beach":
    print ("i love making sandcastles on there!")
  elif wesfav == "pier" or wesfav == "the pier": 
    print ("ahh the arcades are great")
  else:
    print ("ooh wow, ive not been there before!")
else:
  print("oh so you're not from round these parts?")
  
  