print ("🎵FILL IN THE BLANK LYRICS!🎵")
print () 
print ("find out the missing lyric in as less trys as possible!")
print()
counter = 1
while True:
  lyric = input("Never gonna ____ you up. > ")
  print()
  if lyric == "give" or lyric == "Give":
    print ("Never gonna let you down! .. oh yea!")
    print()
    break
  else:
    print("Not quite, try again!")
    print()
    counter +=1
print ()
print("Thanks for playing! You got that in", counter,"trys!")