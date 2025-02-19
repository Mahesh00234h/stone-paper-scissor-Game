import random

print("Welcome to Stone Paper-Scissors game ")
list = ['stone', 'paper', 'scissors']

while True:
    player = input("Enter stone, paper, or scissors : ").lower()
    
    if player == 'quit':
        print("thanks for playing")
        break
    
    if player not in list:
        print("Invalid choice Please try again.")
        continue
    
    ncp = random.choice(list)
    print(f"ncp chose: {ncp}")
    
    if player == ncp:
        print("It is a tie")
    elif player == 'stone' and ncp == 'scissors' or \
         player == 'paper' and ncp == 'stone' or \
         player == 'scissors' and ncp == 'paper':
        print("You wins")
    else:
        print("ncp wins")
