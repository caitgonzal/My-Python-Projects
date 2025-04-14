import random

# top of range
t_range = input("Type a number: ")

if t_range.isdigit():
    t_range = int(t_range)
    if t_range <= 0:
        print("Please type out a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


rand_num = random.randint(0, t_range)
guesses = 0


while True:
    guesses += 1
    # user guess
    u_guess = input("Make a guess: ")

    if u_guess.isdigit():
        u_guess = int(u_guess)
    else:
        print("please type a number next time.")
        continue
    
    if u_guess == rand_num:
        print("You got it right!")
        break
    elif u_guess > rand_num:
        print("You are above the number.")
    else:
        print("You are below the number.")

print("You got it in", guesses, "guesses.")
