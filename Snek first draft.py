#Final project

class room_one:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp
        self.searched = False

    def description(self):
        first_room = open("room1.txt", "r")
        print(first_room.read())
        first_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Go to room 2")
            print()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if self.searched == False:
                    print("You find 2 gold coins.")
                    print()
                    self.wealth += 2
                    self.searched = True
                else:
                    print("You already searched this room.")
                    print()
            elif player_input == 2:
                #still_in_room = False
                #return breaks us out of the loop without needing to change the boolean, but I needed
                #a way to keep the loop going until they left.
                return self.health, self.wealth, 2, False  #change this boolean later
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_two:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp

    def description(self):
        second_room = open("room2.txt", "r")
        print(second_room.read())
        second_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Take the coins from the alcove")
            print("3 - Go to room 3")
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                print("The room is otherwise empty.")
                print()
            elif player_input == 2:
                print("The coins are an illusion, instead a coiled cobra bites you!")
                print("-2 hp!")
                print()
                self.health -= 2
                if self.health <= 0:
                    return self.health, self.wealth, 2, True
            elif player_input == 3:
                return self.health, self.wealth, 3, False
            else:
                print("Invalid choice.  Choose again.")
                print()


class room_three:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp
        self.searched = False
        self.snek_alive = True

    def description(self):
        third_room = open("room3.txt", "r")
        print(third_room.read())
        third_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Fight")
            print("3 - Go to room 4")
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if self.snek_alive == True:
                    print("The Snek Cultist bites you!")
                    print("-1 hp!")
                    self.health -= 1
                    if self.health <= 0:
                        return self.health, self.wealth, 3, True
                elif self.searched == False:
                    print("Among the bones you find 5 gp!")
                    print()
                    self.wealth += 5
                    self.searched = True
                else:
                    print("All you find are the bones of failed adventurers.")
                    print()
            elif player_input == 2:
                if self.snek_alive == True:
                    print("The Snek Cultist bites you, -1 hp!")
                    self.health -= 1
                    if self.health <= 0:
                        return self.health, self.wealth, 2, True
                    print("A vicious uppercut, you knock him out!")
                    print()
                    self.snek_alive = False
                else:
                    print("You kick him while he's down...")
                    print()
            elif player_input == 3:
                if self.snek_alive == True:
                    print("The Snek Cultist blocks your way!")
                    print("The Snek Cultist bites you!  -1 hp!")
                    print()
                    self.health -= 1
                    if self.health <= 0:
                        return self.health, self.wealth, 2, True
                else:
                    return self.health, self.wealth, 4, False
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_four:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp

    def description(self):
        fourth_room = open("room4.txt", "r")
        print(fourth_room.read())
        fourth_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Drink from the fountain")
            print("3 - Make a wish")
            print("4 - Go to room 5")
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                print("The room is otherwise empty.")
                print()
            elif player_input == 2:
                print("Your thirst is slek'd.")
            elif player_input == 3:
                if self.wealth <= 0:
                    print("The gods have abandoned you.")
                    print()
                else:
                    print("You toss a coin in the fountain.")
                    print("You feel like a good person.")
                    print()
                    self.health += 1
                    self.wealth -= 1
            elif player_input == 4:
                return self.health, self.wealth, 5, False
            else:
                print("Invalid choice.  Choose again.")
                print()


class room_five:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp

    def description(self):
        fifth_room = open("room5.txt", "r")
        print(fifth_room.read())
        fifth_room.close()

    def choice(self):
        still_in_room = True
        searched = False

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Gather coins")
            print("3 - Go to room 6")
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if searched == False:
                    print("You discover a tripwire over the walkway.")
                    print("You gently disarm it.")
                    print()
                    searched = True
                else:
                    print("Hissing snakes and untold riches lie below.")
                    print("The room is otherwise empty.")
                    print()
            elif player_input == 2:
                print("Your greed is matched only by your foolishness.")
                print("A thousand coins await, as do a thousand snakes.")
                print("The snakes bite you to death...")
                print()
                self.health = 0
                return self.health, self.wealth, 5, True
            elif player_input == 3:
                if searched == False:
                    print("You trip over a wire. The statues spit blinding venom in your eyes.")
                    print("You stumble and fall off the pathway into the pit of snakes.")
                    print("The snakes bite you to death...")
                    print()
                    self.health = 0
                    return self.health, self.wealth, 5, True
                else:
                    return self.health, self.wealth, 6, False
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_six:

    def __init__(self, hp, gp):
        self.health = hp
        self.wealth = gp

    def description(self):
        sixth_room = open("room6.txt", "r")
        print(sixth_room.read())
        sixth_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - FIGHT!")
            print("2 - Run awaaay!!!")
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                print("The priestess stabs you with her dagger.  -7 hp!")
                self.health -= 7
                if self.health <= 0:
                    return self.health, self.wealth, 6, True
                print("You deliver a haymaker and break her neck!")
                print("You have defeated the Cult of Sotek!")
                print("The golden statue is yours, and will fetch a fine price...")
                self.wealth += 100
                return self.health, self.wealth, 6, True
            elif player_input == 2:
                print("The door locked behind you.  The priestess stabs you in the back.")
                print("You die a coward...")
                print()
                self.health = 0
                return self.health, self.wealth, 6, True
            else:
                print("Invalid choice.  Choose again.")
                print()

def main():
    game_over = False
    health = 10
    gold = 0
    room = 1  #need to initially set to the first room
    #these will need to be passed as variables

    #introduction/title screen

    print("Welcome to Cult of the Snek.")
    print()
    print("You are a brave warrior entering the jungles of Lustria, lured by tales of wealth")
    print("in the ancient Temple of Python.  Beware, for this temple is not abandoned.")
    print("The deadly Cult of the Snek will protect their treasure.")
    print()

    #press any key to begin
    input("Are you ready to begin?  (press <ENTER> to continue)")
    print()

    #read in room 1, print room 1 text
    while game_over == False:
        if room == 1:
            the_room = room_one(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        elif room == 2:
            the_room = room_two(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        elif room == 3:
            the_room = room_three(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        elif room == 4:
            the_room = room_four(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        elif room == 5:
            the_room = room_five(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        elif room == 6:
            the_room = room_six(health, gold)
            the_room.description()
            health, gold, room, game_over = the_room.choice()
        else:
            print ("Wow you REALLY messed up.  Try starting over.")

    #query for action
    #need to move these queries into the room functions?


    #final game screen
    if health <= 0:
        print("Your health is ", health)
        print("The Temple of Sotek claims another victim.")
        print("You lose...")
    else:
        print(health, gold)
        print("***You win!***")


main()
