import random

#colour preset variables
default = "\033[0m"
green = "\033[32m"
red = "\033[31m"
yellow = "\033[33m"
purp = "\033[35m"
cyan = "\033[36m"

#Guess Game Start:
print ("*~* 🔢 Guess the number between 0-1000 🔢 *~*")
print()
AnswerNum = random.randint (0,100)
counter = 1
while True:
  guess = int(input("What's your guess? 🤔 > "))
  print()
  if guess < 0: 
    print ("❌ Minus!!😑Thats way too low.. i'm out!⛔")
    exit()
  if guess < AnswerNum:
    print("❌ Too low...try again!")
    print()
    counter+=1
  elif guess > AnswerNum:
    print ("❌ Too high...try again!")
    print()
    counter+=1
  elif guess == AnswerNum:
    print (yellow,"🎊🎉Wow!🤩 You got it!🎉🎊", default)
    break
  else: 
    print ("Thats not between 1000!")
print()
print("Thanks for playing! You got that in",purp,counter,default,"attempt(s)!")