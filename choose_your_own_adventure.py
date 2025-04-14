while True:
    name = input("Hello adventurer. What is your name: ")
    print(" Welcome", name, "to your adventure!")

    answer = input("You are at a fork road, you can go left or right. Which way would you like to go? (left/right) ").lower()

    if answer == "left":
        answer = input("You are at a river, you can walk around or swim across. Which way would you like to go? (walk/swim) ").lower()
        if answer == "walk":
            answer = input("You are tired from the walk but see a traveler ahead. Do you stop to converse with them or continue on your journey? (converse/continue) ").lower()
            if answer == "converse":
                print("The traveler asks if you have any spare gold, he was robbed by thieves a few moons ago. You check your pouch, you have 15 gold. Care to share?")
                answer = input("How much gold are you willing to give the traveler? (none/half/all) ").lower()
                if answer == "none":
                    print("The traveler saw how much gold you had in your pouch, he did not like that you weren't willing to spare any.")
                    print("The traveler snuck behind you and turned you into swiss cheese.")
                    print("You died, see you in the next life.")
                    quit()
                elif answer == "half":
                    print("The traveler thanks you for your kindness and asks if you need directions for your journey")
                    
                    while True:
                        answer = input("There are 2 choices you have, the king's palace or the forbidden forest of fortune, what destination do you seek? (palace/fortune) ").lower()
                        if answer == "palace":
                            print("The traveler gives you directions to your journey. Unfortunately that led to an ambush.")
                            print("You died, see you in the next life.")
                            break
                        elif answer =="fortune":
                            print("You head to the forest.")
                            print("While it took you 2 moons and 3 suns to reach it. You found not only the forest but the secret fortune lying in the center of it.")
                            print("Congrats you won the game")
                            break
                        else:
                            print("Not a valid option")
                            print("Let's start from the beginning since you can't follow directions.")
                            continue
                elif answer == "all":
                    print("The traveler sees he was able to easily get all your money from you.")
                    print("As you turn your head to check your surroundings the traveler sneaks behind you and stabs you.")
                    print("You died, see you in the next life.")
                    break
                else:
                    print("Not a valid option")
                    print("Let's start from the beginning since you can't follow directions.")
                    continue
            elif answer == "continue":
                print("The traveler snuck behind you and turned you into swiss cheese.")
                print("You died, see you in the next life.")
                break
            else:
                print("Not a valid option")
                print("Let's start from the beginning since you can't follow directions.")
                continue
        elif answer == "swim":
            print("You drown.")
            break
        else:
            print("Not a valid option")
            print("Let's start from the beginning since you can't follow directions.")
            continue
    elif answer == "right":
        print("You walk off a cliff...it was disguised under bushes.")
        print("You couldn't fly but now you earned your wings...the hard way")
        print("You died, see you in the next life.")
        break
    else:
        print("Not a valid option")
        print("Let's start from the beginning since you can't follow directions.")
        continue
    break