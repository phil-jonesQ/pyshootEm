import random


def main():
    # Game Variables
    run = True # Used for the main loop
    player1_turn = 1 # player 1 starts on turn 1
    player2_turn = 1 # player 2 starts on turn 1
    player_throws = 2 # players have 2 goes but the way the game is coded means it's easy to add many more throws
    my_message = {1: "first", 2: "second"} # Create a dictionary so we can do a more inteligent message to the user
    result = {} # Create an empty dictionary to track the game results

    # A function that represents a dice throw
    def throw():
        return random.randrange(1, 6)

    # Main game loop
    while run is True:
        while player1_turn <= player_throws: # Repeat for how many throws we get
            input("Player 1 press enter to throw your " + str(my_message.get(player1_turn)) + " die..")
            my_throw = throw() # Call our throw function and store in a variable
            print ("Player 1 has thrown a " + str(my_throw)) # Print the result
            d = {"player1 throw " + str(player1_turn): my_throw} # Prepare add the result to the result dictionary
            result.update(dict(d)) # update it
            player1_turn = player1_turn + 1 # increment the players turn
            print("") # White space

        # Code is the same so really we should refactor it to be just one while loop
        while player2_turn <= player_throws:
            input("Player 2 press enter to throw your " + str(my_message.get(player2_turn)) + " die..")
            my_throw = throw()
            print ("Player 2 has thrown a " + str(my_throw))
            d = {"player2 throw " + str(player2_turn): my_throw}
            result.update(dict(d))
            player2_turn = player2_turn + 1
            print("")

        # Totals simply extract the result from  the dictionary
        #print (result) ## Uncomment to see what the dictionary looks like
        player1_total = result['player1 throw 1'] + result['player1 throw 2']
        player2_total = result['player2 throw 1'] + result['player2 throw 2']

        print("Player 1 got " + str(player1_total))
        print("Player 2 got " + str(player2_total))

        # Logic to see who won or if it was a draw
        if player1_total == player2_total:
            print ("Game was drawn!!")
        else:
            if player1_total > player2_total:
                print ("Player 1 WON!!")
            else:
                print ("Player 2 WON!!")
        run = False # Stop main loop

        # Restart game
        input ("Press Enter to play again...")
        print ("")
        print ("")
        main()
# Call main game
main()


