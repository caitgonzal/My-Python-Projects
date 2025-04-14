print("Welcome to the quiz game. Let's see how much you know about the world!")

playing = input("Do you want to play? (yes/no) ")

if playing != "yes":
    print("Okay, maybe next time.")
    quit()

name = input("What is your name? ")

print("Hi,", name, "Let's play!")
score = 0

# Question 1
answer = input("What does USA stand for? ")
if answer.lower() == "united states of america":
    score += 1
    print("Correct, your score is currently " + str(score) +". Let's, go to the next question!")
else:
    print("Incorrect, your score is currently " + str(score) +". Let's, go to the next question!")

# Question 2
answer = input("What does UK stand for? ")
if answer.lower() == "united kingdom":
    score += 1
    print("Correct, your score is currently " + str(score) +". Let's, go to the next question!")
else:
    print("Incorrect, your score is currently " + str(score) +". Let's, go to the next question!")

# Question 3
answer = input("What does EU stand for? ")
if answer.lower() == "european union":
    score += 1
    print("Correct.")
else:
    print("Incorrect.")

print("Your final score is " + str(score) + " out of 3.")

# Quiz Complete
percent = float((score / 3) * 100)
print("You got " + f"{percent:.2f}" + "%")
print("Thank you for playing the quiz game!")