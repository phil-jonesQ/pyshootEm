import random


def main():
    # Game Variables
    run = True # Used for the main loop
    players_turn = 1 # player 1 starts on turn 1
    total_player_throws = 4 # players have 2 goes each
    round = 1 # round system
    round_max = 4
    my_message = {1: "Player 1, press enter to throw your first die", 2: "Player 1, press enter to throw your second die",
                  3: "Player 2 press enter to throw your first die", 4: "Player 2, press enter to throw your second die"} # Create a dictionary so we can do a more inteligent message to the user
    my_player_map = {1: "Player 1", 2: "Player 1", 3: "Player 2", 4: "Player 2"}
    result = {} # Create an empty dictionary to track the game results

    # A function that represents a dice throw
    def throw():
        return random.randrange(1, 6)

    # Main game loop
    while run is True:
        while round <= round_max:
            print ("#####################################")
            print ("Playing round " + str(round))
            print ("#####################################")
            while players_turn <= total_player_throws: # Repeat for how many throws we get
                input(str(my_message.get(players_turn))) # Wait for return key
                my_throw = throw() # Call our throw function and store in a variable
                print (my_player_map.get(players_turn) + " threw a " + str(my_throw)) # Print the result
                d = {my_player_map.get(players_turn) + " count " + str(players_turn) + " for round " + str(round): my_throw} # Prepare add the result to the result dictionary
                result.update(dict(d)) # update it
                players_turn += 1 # increment the players turn
                print("") # White space

            # Totals simply extract the result from  the dictionary
            print (result)
            player1_total = result['Player 1 count 1 for round ' + str(round)] + result['Player 1 count 2 for round ' + str(round)]
            player2_total = result['Player 2 count 3 for round ' + str(round)] + result['Player 2 count 4 for round ' + str(round)]

            print("Player 1 got " + str(player1_total))
            print("Player 2 got " + str(player2_total))

            # Logic to see who won or if it was a draw
            if player1_total == player2_total:
                print ("Round was drawn!!")
            else:
                if player1_total > player2_total:
                    print ("Player 1 WON Round " + str(round) + "!!!")
                else:
                    print ("Player 2 WON Round " + str(round) + "!!!")

            round += 1
            players_turn = 1
            print ("DEBUG round: " + str(round) + " turns var: " + str(players_turn))


        # Restart game
        print (result)  ## Uncomment to see what the dictionary looks like
        print ("#####################################")
        input ("Rounds over, Press Enter to play again...")
        print ("#####################################")
        print ("")
        print ("")
        run = False  # Stop main loop
        main()
# Call main game
main()


