exit = "no"

while exit == "no":
  print ()
  animal = input ("What animal do you want to hear? > ")
  print ()
  if animal == "cow" or animal == "Cow":
    print ("Mooo!!🐄")
  elif animal == "pig" or animal == "Pig":
    print ("Oink!!🐷")
  elif animal == "sheep" or animal == "Sheep":
    print ("Baaa!!🐑")
  elif animal == "cat" or animal == "Cat":
    print ("Meow!!🐈")
  elif animal == "dog" or animal == "Dog":
    print ("Woof!!🐕")
  elif animal == "duck" or animal == "Duck":
    print ("Quack!!🦆")
  elif animal == "snake" or animal == "Snake":
    print ("SSSssss!!🐍")
  else:
    print("I don't know that animal sound. Try again.")
  print ()
  exit = input("Do you want to exit?: ")
print ()
print ("Ok, goodbye!")