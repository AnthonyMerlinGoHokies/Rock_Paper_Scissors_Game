import random

def get_choices(): #creates a function
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["paper","rock","scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}
  
  return choices 

def check_win(player, computer):
  print (f"You choose {player}, computer chooses {computer} ")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You Win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You Win!."
    else:
      return "Sissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Paper covers rock! You Win!"
    else:
      return "Rock smashes paper! You lose."

choices = get_choices()
result = check_win (choices["player"],choices["computer"])
print (result)




#////////////////////////////////////////////////////
# check_win("rock","paper") 
#checks the check_win function with rock as player and paper as computer
#////////////////////////////////////////////////////
#example of else and elif statements 
#age = 20 
#if age >= 18 
#  print("You are an adult.")
#elif age > 12
#  print("You are a teenager.")
#elif age > 1
#  print ("You are a child.")
#else 
#  print ("You are a baby")
#////////////////////////////////////////////////////
# example of f strings
#age = 25 
#print (f:"Jim is {age} years old.")
#////////////////////////////////////////////////////
#choices = {"player": "rock","computer": "paper"}
#p_choice = choices["player"]
#gets the choice of the player
