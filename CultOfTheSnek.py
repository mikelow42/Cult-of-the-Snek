#Final project

from random import randrange

class player:

    def __init__(self):
        self.hp = 10
        self.gp = 0
        self.searched_one = False
        self.searched_3 = False
        self.searched_5 = False
        self.killed_snek = False

    def prompt(self):
        print("HP: ", self.hp, "// Gold: ", self.gp)

class room_one:

    def __init__(self, player_object):
        self.player = player_object

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
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if self.player.searched_one == False:
                    print("You find 2 gold coins.")
                    print()
                    self.player.gp += 2
                    self.player.searched_one = True
                else:
                    print("You already searched this room.")
                    print()
            elif player_input == 2:
                #still_in_room = False
                #return breaks us out of the loop without needing to change the boolean, but I needed
                #a way to keep the loop going until they left.
                return self.player, 2, False  #change this boolean later
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_two:

    def __init__(self, player_object):
        self.player = player_object

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
            print("4 - Go back")
            print()
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                print("The room is otherwise empty.")
                print()
            elif player_input == 2:
                print("The coins are an illusion, instead a coiled cobra bites you!")
                print("-2 hp!")
                print()
                self.player.hp -= 2
                if self.player.hp <= 0:
                    return self.player, 2, True
            elif player_input == 3:
                return self.player, 3, False
            elif player_input == 4:
                return self.player, 1, False
            else:
                print("Invalid choice.  Choose again.")
                print()


class room_three:

    def __init__(self, player_object):
        self.player = player_object

    def description(self):
        if self.player.killed_snek == False:
            third_room = open("room3.txt", "r")
            print(third_room.read())
            third_room.close()
        else:
            third_room = open("room3_deadsnek.txt", "r")
            print(third_room.read())
            third_room.close()

    def choice(self):
        still_in_room = True
        bite = 0
        snek = 2

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Fight")
            print("3 - Go to room 4")
            print("4 - Go back")
            print()
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if self.player.killed_snek == False:
                    bite = randrange(1,3)
                    print("The Snek Cultist bites you!")
                    print("You lose ", bite, " hp!")
                    self.player.hp -= bite
                    if self.player.hp <= 0:
                        return self.player, 3, True
                elif self.player.searched_3 == False:
                    print("Among the bones you find 5 gp!")
                    print()
                    self.player.gp += 5
                    self.player.searched_3 = True
                else:
                    print("All you find are the bones of failed adventurers.")
                    print()
            elif player_input == 2:
                if self.player.killed_snek == False:
                    bite = randrange(1,3)
                    print("The Snek Cultist bites you!")
                    print("You lose ", bite, " hp!")
                    self.player.hp -= bite
                    if self.player.hp <= 0:
                        return self.player, 3, True
                    snek -= randrange(1,3)
                    if snek <= 0:
                        print("A vicious uppercut, you knock him out!")
                        print()
                        self.player.killed_snek = True
                    else:
                        print("You land a solid punch!")
                else:
                    print("You kick him while he's down...")
                    print()
            elif player_input == 3:
                if self.player.killed_snek == False:
                    bite = randrange(1,3)
                    print("The Snek Cultist blocks your way!")
                    print("The Snek Cultist bites you!")
                    print("You lose ", bite, " hp!")
                    print()
                    self.player.hp -= bite
                    if self.player.hp <= 0:
                        return self.player, 3, True
                else:
                    return self.player, 4, False
            elif player_input == 4:
                if self.player.killed_snek == False:
                    bite = randrange(1,3)
                    print("The Snek Cultist blocks your way!")
                    print("The Snek Cultist bites you!")
                    print("You lose ", bite, " hp!")
                    print()
                    self.player.hp -= bite
                    if self.player.hp <= 0:
                        return self.player, 3, True
                else:
                    return self.player, 2, False
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_four:

    def __init__(self, player_object):
        self.player = player_object

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
            print("5 - Go back")
            print()
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                print("The room is otherwise empty.")
                print()
            elif player_input == 2:
                print("Your thirst is slek'd.")
            elif player_input == 3:
                if self.player.gp <= 0:
                    print("The gods have abandoned you.")
                    print()
                else:
                    print("You toss a coin in the fountain.")
                    print("You feel like a good person.")
                    print()
                    self.player.hp += 1
                    self.player.gp -= 1
            elif player_input == 4:
                return self.player, 5, False
            elif player_input == 5:
                return self.player, 3, False
            else:
                print("Invalid choice.  Choose again.")
                print()


class room_five:

    def __init__(self, player_object):
        self.player = player_object

    def description(self):
        fifth_room = open("room5.txt", "r")
        print(fifth_room.read())
        fifth_room.close()

    def choice(self):
        still_in_room = True

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - Search the room")
            print("2 - Gather coins")
            print("3 - Go to room 6")
            print("4 - Go back")
            print()
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                if self.player.searched_5 == False:
                    print("You discover a tripwire over the walkway.")
                    print("You gently disarm it.")
                    print()
                    self.player.searched_5 = True
                else:
                    print("Hissing snakes and untold riches lie below.")
                    print("The room is otherwise empty.")
                    print()
            elif player_input == 2:
                print("Your greed is matched only by your foolishness.")
                print("A thousand coins await, as do a thousand snakes.")
                print("The snakes bite you to death...")
                print()
                self.player.hp = 0
                return self.player, 5, True
            elif player_input == 3:
                if self.player.searched_5 == False:
                    print("You trip over a wire. The statues spit blinding venom in your eyes.")
                    print("You stumble and fall off the pathway into the pit of snakes.")
                    print("The snakes bite you to death...")
                    print()
                    self.player.hp = 0
                    return self.player, 5, True
                else:
                    return self.player, 6, False
            elif player_input == 4:
                return self.player, 4, False
            else:
                print("Invalid choice.  Choose again.")
                print()

class room_six:

    def __init__(self, player_object):
        self.player = player_object

    def description(self):
        sixth_room = open("room6.txt", "r")
        print(sixth_room.read())
        sixth_room.close()

    def choice(self):
        still_in_room = True
        priestess = 4
        bite = 0

        while still_in_room == True:
            print("What would you like to do?")
            print("1 - FIGHT!")
            print("2 - Run awaaay!!!")
            print()
            self.player.prompt()
            player_input = eval(input("Input the number of your choice: "))
            print()

            if player_input == 1:
                bite = randrange(1,5)
                print("The priestess stabs you with her dagger.")
                print("You lose ", bite, " hp!")
                self.player.hp -= bite
                if self.player.hp <= 0:
                    return self.player, 6, True
                priestess -= randrange(1,3)
                if priestess <= 0:
                    print("You deliver a haymaker and break her neck!")
                    print("You have defeated the Cult of Sotek!")
                    print("The golden statue is yours, and will fetch a fine price...")
                    self.player.gp += 100
                    return self.player, 6, True
                else:
                    print("You land a punch but she hisses defiantly.")
            elif player_input == 2:
                print("The door locked behind you.  The priestess stabs you in the back.")
                print("You die a coward...")
                print()
                self.player.hp = 0
                return self.player, 6, True
            else:
                print("Invalid choice.  Choose again.")
                print()

def main():
    game_over = False
    room = 1  #need to initially set to the first room

    player_one = player()
    #player object will pass back and forth and keep track of variable values.
    #introduction/title screen

    print("Welcome to Cult of the Snek.")
    print()
    print("You are a brave warrior entering the jungles of Lustria, lured by tales of wealth")
    print("in the ancient Temple of Python.  Beware, for this temple is not abandoned.")
    print("The deadly Cult of the Snek will protect their treasure.")
    print()

    #press any key to begin
    player_one.prompt()
    input("Are you ready to begin?  (press <ENTER> to continue)")
    print()

    #read in room 1, print room 1 text
    while game_over == False:
        if room == 1:
            the_room = room_one(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        elif room == 2:
            the_room = room_two(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        elif room == 3:
            the_room = room_three(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        elif room == 4:
            the_room = room_four(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        elif room == 5:
            the_room = room_five(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        elif room == 6:
            the_room = room_six(player_one)
            the_room.description()
            player_one, room, game_over = the_room.choice()
        else:
            print ("Wow you REALLY messed up.  Try starting over.")


    #final game screen
    if player_one.hp <= 0:
        player_one.prompt()
        print("The Temple of Sotek claims another victim.")
        print("You lose...")
    else:
        player_one.prompt()
        print("***You win!***")


main()
