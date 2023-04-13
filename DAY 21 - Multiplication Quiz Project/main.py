print ("""=x= Multiplication Quiz =x= 

Do you know your timestables?""")
print ()
#counter set up
counter = 0
#user input and code for test:
NumChoice = int(input ("What number do you want to test up to a multiple of 10? > "))
print()
for i in range (1,11,):
  correct = i* NumChoice
  print ()
  print (i,"x", NumChoice)
  answer = int(input("> "))
  if answer == correct:
    print()
    print("Thats Right!😃")
    counter += 1
  else:
    print()
    print ("Im afraid thats not the right answer.☹️ It should have been", correct)

if counter == 10:
  print ()
  print("😱 Wow, you got them all right!🥳🥳")
else:
  print ()
  print ("You got" , counter, "out of the 10 questions right.")