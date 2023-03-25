from getpass import getpass as input
print(" ROCK⛰, PAPER📄, SCISSORS✂️ BATTLE! ")
print("""
Select your Move! Type:

R = Rock
P = Paper
S = Scissors

Then, press enter.""")
print()
print()
player1 = input("Player 1, your move > ")
print()
player2 = input("Player 2, your move >  ")
print()
if player1 == "R" or player1 == "r":
  if player2 == "R" or player2 == "r":
    print("Its a Draw! You both picked Rock!")
  elif player2 == "P" or player2 == "p":
    print("Paper beats Rock, Player 2 wins!")
  elif player2 == "S" or player2 == "s":
    print("Rock beats Scissors, Player 1 wins!")
  else:
    print ("Not heard of that one before Player 2.. please re-run!")
elif player1 == "P" or player1 == "p":
  if player2 == "P" or player2 == "p":
    print("Its a Draw! You both picked Paper!")
  elif player2 == "R" or player2 == "r":
    print("Paper beats Rock, Player 1 wins!")
  elif player2 == "S" or player2 == "s":
    print("Scissors beats paper, Player 2 wins!")
elif player1 == "S" or player1 == "s":
  if player2 == "S" or player2 == "s":
    print("Its a Draw! You both picked scissors!")
  elif player2 == "R" or player2 == "r":
    print("Rock beats Scissors, Player 2 wins!")
  elif player2 == "P" or player2 == "p":
    print("Scissors beats paper, Player 1 wins!")
  else:
    print ("Not heard of that one before Player 2.. please re-run!")
else:
    print ("Not heard of that one before Player 1.. please re-run!")