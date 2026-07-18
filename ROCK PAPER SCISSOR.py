import random
choices = ["rock","paper","scissors"]
user_score=0
computer_score=0
print("Welcome to rock,paper,scissors game!")
print("Type quit to exit the game.")
while True:
   user_choice=input("Enter your choice (rock, paper, scissors): ").lower()
   if user_choice=='quit':
    print(f"Thanks for playing...\n Your score : {user_score} \n Computer's score : {computer_score}")
    break
   
   if user_choice not in choices:
    print("Invalid choice.Please try again.")
    continue
   
   computer_choice=random.choice(choices)
   print(f"Computer chose: {computer_choice}")
   if user_choice == computer_choice:
    print("Its a tie.")
   elif (user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper"):
    print("Congratulations! You win!")
    user_score += 1
   else:
    print("Sorry! You lose.")
    computer_score +=1
   print(f"Your score : {user_score} \nComputer's score : {computer_score}")


    
    
    
   
   
    




