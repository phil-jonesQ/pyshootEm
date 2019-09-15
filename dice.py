""" Version 1.03 - Simple chance game using rounds and two players - records results
game features while loops to stop code repetition and dictionaries to generate messages and record results
"""


import random


def main():
    # Game Variables
    run = True  # Used for the main loop
    players_turn = 1  # player 1 starts on turn 1
    total_player_throws = 4  # players have 2 goes each
    rounds = 1  # rounds system
    round_max = 9  # Max rounds
    my_message = {1: "Player 1, press enter to throw your first die",
                  2: "Player 1, press enter to throw your second die",
                  3: "Player 2, press enter to throw your first die",
                  4: "Player 2, press enter to throw your second die"}
    # Create a dictionary so we can do a more inteligent message to the user
    my_player_map = {1: "Player 1", 2: "Player 1", 3: "Player 2", 4: "Player 2"}
    result = {}  # Create an empty dictionary to track the game results
    round_result = {}  # Easily record each rounds result in another dictionary

    # A function that represents a dice throw
    def throw():
        return random.randrange(1, 6)

    # Main game loop
    while run is True:
        while rounds <= round_max:
            print("#####################################")
            print("Playing round " + str(rounds))
            print("#####################################")
            while players_turn <= total_player_throws:  # Repeat for how many throws we get
                input(str(my_message.get(players_turn)))  # Wait for return key
                my_throw = throw() # Call our throw function and store in a variable
                print(my_player_map.get(players_turn) + " threw a " + str(my_throw))  # Print the result
                # Prepare add the result to the result dictionary
                d = {my_player_map.get(players_turn) + " count " + str(players_turn) + " for round " + str(rounds): my_throw}
                result.update(dict(d))  # update it
                players_turn += 1  # increment the players turn
                print("")  # White space

            # Totals simply extract the result from  the dictionary

            player1_total = result['Player 1 count 1 for round ' + str(rounds)] + result['Player 1 count 2 for round ' + str(rounds)]
            player2_total = result['Player 2 count 3 for round ' + str(rounds)] + result['Player 2 count 4 for round ' + str(rounds)]

            print("Player 1 got " + str(player1_total))
            print("Player 2 got " + str(player2_total))

            # Logic to see who won the round or if it was a draw
            if player1_total == player2_total:
                print("Round was drawn!!")
                rd = {"Round " + str(rounds) + " was a draw": 0}
            else:
                if player1_total > player2_total:
                    print("Player 1 WON Round " + str(rounds) + "!!!")
                    rd = {"Round " + str(rounds) + " went to Player 1": 1}  # Add a player one key and value 1
                else:
                    print("Player 2 WON Round " + str(rounds) + "!!!")
                    rd = {"Round " + str(rounds) + " went to Player 2": 2}  # Add a player two key and value 2

            # Record the result
            rounds += 1  # Increment the rounds
            players_turn = 1  # Reset the turns back to 1 so the next round will work
            round_result.update(dict(rd))  # update the result for later on

        print("#####################################")
        print("Rounds over, Press Enter for results and to play again...")
        input("")
        player1_wins = 0  # New var to capture the wins
        player2_wins = 0
        for result in round_result:  # Loop over the round_results dictionary
            if round_result[result] == 1:  # If the value is a 1 then increment a player 1 win
                player1_wins += 1
            if round_result[result] == 2:  # If the value is a 2 then increment a player 2 win
                player2_wins += 1
            # Dump results
            print(result)
        # Summarise totals
        print("Player 1 won " + str(player1_wins) + " times..")
        print("Player 2 won " + str(player2_wins) + " times..")

        # Logic to print a summary of overall winner
        if player1_wins == player2_wins:
            print("")
            print("Overall player 1 and player 2 have drawn")
            print("")
        else:
            if player1_wins > player2_wins:
                print("")
                print("Overall player 1 won more rounds")
                print("")
            else:
                print("")
                print("Overall player 2 won more rounds")
                print("")

        print("#####################################")
        print("")
        print("")

        run = False  # Stop main loop
        main()


# Call main game
main()



