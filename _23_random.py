# Random built in function in python
'''
    random ka randomness (randomness = unpredictable/accidental selection) security
    purposes ke liye suitable nahi hota. Passwords, security tokens, etc. 
    ke liye secrets module use hota hai.

    random function ko use karnay kay liya is function ko import karna parta hay
    import random
'''
print("------------------")
import random
y=random.random() #its range 0.0 to 1.0
print(y)

print("------------------")
# randint(start,stop) but give olny one value return
x=random.randint(1,19)
print(x)

print("------------------")
print("for dice example ")
dice=random.randint(1,6)
print(f"you rolled the dice and the dice number is {dice}")
print("for two or more dice : example ")
for x in range(2):
    m_dice=random.randint(1,6)
    print(m_dice)

print("------------------")
# random.randrange bi same randint ki terhain hota hay 
# randrange(start,stop,step)
a=random.randrange(0,20,2) #it gives only even number
print(a)

print("------------------")
print("chossing random item from list we use random.choice() ")
colour=['red','pink','yellow','black','blue','green','orange']
color=random.choice(colour)  #choice select only one item
print('the single random colour :',color)
colors=random.choices(colour,k=3)  #choose the multiple items from the list 
print('the multiple random colours :',colors)


print("------------------")
print("for chose the random one letter ")
letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(letter)

print("------------------")
# sample in random is same like the choices
students = ["Ali", "Ahmed", "Hasnain", "Usman", "Bilal"]
result = random.sample(students, k=2)
result1 = random.choices(students, k=2)
print(result)
print(result1)

print("------------------")
# shuffle() list ke items ko randomly rearrange karta hai.
playing_card=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
random.shuffle(playing_card)
print(playing_card)

print("------------------")
# random.seed()
# Ab ek important advanced concept.
print("normaly we use randint different result gives  ",random.randint(1,20))
print("advance we use seed,it produce the same sequence   ")
random.seed(100)
print(random.randint(1, 100))

'''
    seed() ka Use Kyun?
    Ye especially:
        Testing
        Machine Learning experiments
        Simulations
        Debugging
        Reproducible results
    mein useful hai.
'''
print("------------------")
random.seed(50)
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print(numbers)

print("------------------")
"""create the simple game using random function """
print("game")
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print(".................................")
print("   ROCK PAPER SCISSORS GAME")
print(".................................")
while True:
    print("Choose any one option :")
    print("      1. Rock")
    print("      2. Paper")
    print("      3. Scissors")
    print("      0. Exit")
    user_choice = input("Enter your choice: ")
    # Exit
    if user_choice == "0":
        print("Game Over!")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        break
    # Check input
    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue
    
    # Convert number to choice

    user = choices[int(user_choice) - 1]
    # Computer randomly chooses
    computer = random.choice(choices)
    print("\nYou chose:", user)
    print("Computer chose:", computer)
    
    # Decide winner
    if user == computer:
        print("🤝 Draw!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💻 Computer Wins!")
        computer_score += 1
    print("Score:", user_score, "-", computer_score)

