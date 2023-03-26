from getpass import getpass as input
print("ROCK⛰ , PAPER📄, SCISSORS✂️  BATTLE! ")
print("""
Select your Move! Type one of the following:

R = Rock
P = Paper
S = Scissors

(Then, press enter.)""")
print()
print ("Lets Begin!...")
print()
#counter for score:
player1_score = 0
player2_score = 0
# using while loop
while True:
  player1 = input("🟦 Player 1 , your move > ")
  print()
  player2 = input("🟥 Player 2 , your move >  ")
  print()
  if player1 == "R" or player1 == "r":
    if player2 == "R" or player2 == "r":
      print("Its a Draw! No points.😬 You both picked Rock!⛰")
    elif player2 == "P" or player2 == "p":
      print("Paper beats Rock, Player 2 wins!🟥📄")
      player2_score +=1
    elif player2 == "S" or player2 == "s":
      print("Rock beats Scissors, Player 1 wins!🟦 ⛰") 
      player1_score +=1
    else:
      print ("Not heard of that one before Player 2 😬.. Lets start again!")
  elif player1 == "P" or player1 == "p":
    if player2 == "P" or player2 == "p":
      print("Its a Draw! No points.😬 You both picked Paper!📄")
    elif player2 == "R" or player2 == "r":
      print("Paper beats Rock, Player 1 wins!🟦📄")
      player1_score +=1
    elif player2 == "S" or player2 == "s":
      print("Scissors beats paper, Player 2 wins!🟥✂️")
      player2_score +=1
  elif player1 == "S" or player1 == "s":
    if player2 == "S" or player2 == "s":
      print("Its a Draw!😬 No Points. You both picked scissors!✂️")
    elif player2 == "R" or player2 == "r":
      print("Rock beats Scissors, Player 2 wins!🟥⛰")
      player2_score +=1
    elif player2 == "P" or player2 == "p":
      print("Scissors beats paper, Player 1 wins!🟦✂️")
      player1_score +=1
    else:
      print ("Not heard of that one before Player 2 😬.. Lets start again!")
  else:
    print ("Not heard of that one before Player 1 😬.. Lets start again!")
  print()
  print("- Player 1 has", player1_score, "wins.")
  print("- Player 2 has", player2_score, "wins.")
  print()
  if player1_score==3 or player2_score==3:
    print ()
    print("Thanks for playing!")
    exit()
  else:
    continue