import random

# This program
# 1. allows players to play multiple rounds
# 2. tracks high scores across games
# 3. displays the high score at the end of the game.

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        print ("Welcome to DUNGEON ADVENTURE!!!")
        print ("This is a muti round game!!")
        print ("What is your name?")
        player_name = str(input())
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player_info = {
            "name":player_name,
            "health":10,
            "inventory":[],
        }
        # print (player_info)
        # TODO: Return the dictionary
        return player_info

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasure_names = {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }

        # TODO: Return the dictionary
        return treasure_names

    def create_all_rounds():
        all_rounds = []
        return all_rounds
    
    def create_high_score_round():
        high_score_round = {
                    "round": 0,
                    "health": 0,
                    "score": 0,
                    "treasure": ""
                }

        # Return the dictionary
        return high_score_round


    def display_options(room_number, round_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print (f"Round number {round_number} - room number {room_number}")
        print ("What would you like to do?")
        print ("    1. Search for treasure")
        print ("    2. Move to next room")
        print ("    3. Check health and inventory")
        print ("    4. Quit the game")

    def search_room(player, treasures, round_number):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        random_outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        if random_outcome == "trap":
            player_health = player.get("health") - 2
        else:
            # the following code selects only key 
            # treasure_gained= random.choice(list(treasures))
            # the following code selects only key & value both
            treasure_gained= random.choice(list(treasures.items()))
        # TODO: Update player dictionary accordingly
        if random_outcome == "trap":
            player["health"] = player_health
        else:
            player["inventory"].append(treasure_gained)
        # TODO: Print messages describing what happened
        if random_outcome == "trap":
            print ("I am sorry, you are TRAPPED!! You have lost 2 health points :(")
        else:
            print (f"Nice job!!!, you have gained a treasure - {treasure_gained[0]}!!!")


    def check_status(player, round_number):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        print ("")
        print (f"Round number {round_number}")
        print (f"Your health now is {player.get("health")}")
        # TODO: If the inventory list is not empty, print items joined by commas
        # print(player)
        if len(player["inventory"]) > 0:
            print ("You have gained ", end="")
            counter = 0
            for key,val in player["inventory"]:
                print (key, end="")
                counter +=1
                if len(player["inventory"]) > 1:
                    if counter+1 == len(player["inventory"]):
                        print (" & ", end="")
                    else:
                        if counter < len(player["inventory"]):
                            print (" , ", end = "")
            print (" so far")

        else:
            # TODO: Otherwise print “You have no items yet.”
            print ("You have no items yet.")

    def print_all_round_info(all_rounds):
        print ("")
        print ("<------------------------ All Rounds Result So far ---------------------------------->")
        print ("Round Number  Health  Total Value  Treasures Collected")
        print ("------------  ------  -----------  ---------------------------------------------------") 
        for round_data in all_rounds:
            print (f"     {round_data["round"]}           {round_data["health"]}", end="")
            print (f"         {round_data["score"]}      {round_data["treasure"]}")
        print ("------------  ------  -----------  ---------------------------------------------------") 
        print ("")

    def end_round(player, treasures, round_number, all_rounds, high_score_round ):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        total_score = 0
        for key, value in player["inventory"]:
            total_score += value
        # TODO: Print final health, items, and total value
        print ("")
        print (f"Round number {round_number}")
        print (f"Your final health is {player["health"]}")
        count = len(player["inventory"])
        # Store all treasures gained
        treasure_gained = ""
        if count > 0:
            print (f"Your total value of treasures is {total_score}")
            print ("You have gained ", end="")
            # counter to determine "," or "&" 
            counter = 0
            for key, value in player["inventory"]:
                print (key, end="")
                treasure_gained += key
                counter+=1
                if len(player["inventory"]) > 1:
                    if counter+1 == len(player["inventory"]):
                        print (" & ", end="")
                        treasure_gained += " & "
                    else:
                        if counter < len(player["inventory"]):
                            treasure_gained += " , "
                            print (" , ", end ="")
            print (" Nice job!!")
        else:
            print ("Sorry, you did not gain any treasure")
            treasure_gained = "You did not gain any treasure in this round"

        # Store high_score_round values
        if total_score > high_score_round["score"]:
            high_score_round["round"] = round_number
            high_score_round["health"] = player["health"]
            high_score_round["score"] = total_score
            high_score_round["treasure"] = treasure_gained

        # update round information
        round_dict = {"round":round_number,
            "health" : player["health"],
            "score" : total_score,
            "treasure" : treasure_gained }
        all_rounds.append(round_dict)

        print_all_round_info(all_rounds)
               
        # TODO: End with a message like "Game Over! Thanks for playing."
        #print (f"Game over {player["name"]}! THANK YOU for playing.. see you next time!")

    def print_high_score_round(high_score_round):
        print ("")
        print ("Your highest score round information")
        print (f"Round number    : {high_score_round["round"]}")
        print (f"Health          : {high_score_round["health"]}")
        print (f"Total Value     : {high_score_round["score"]}")
        print (f"Trasures gained : {high_score_round["treasure"]}")
        print ("")

    def run_game_loop(player, treasures, all_rounds, high_score_round ):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        round_number = 0
        while round_number >= 0:
            round_number +=1
            for i in range(1,6):
            # TODO: Inside each room, prompt player choice using input()
                while i > 0:
                    display_options(i, round_number)
                    choice = input().upper().strip()
            # TODO: Use if/elif to handle each choice (1–4)
                    if choice >= "1" and choice <= "4":
                        if choice == "1":
                            search_room(player, treasures, round_number)
                            break
                        elif choice == "2":
                            print (f"You have skipped room number {i}")
                            break
                        elif choice == "3":
                            check_status(player, round_number)
                        else:
                            break
                    else:
                        print ("Please select option between 1 and 4 only, try again!")
            # TODO: Break or return appropriately when player quits or dies
                if choice == "4" or player["health"] == 0:
                    break
            # TODO: Call end_game() after all rooms are explored
            end_round(player, treasures, round_number, all_rounds, high_score_round )
            while round_number >= 0:
                print ("Do you want to play another round? Type Y for Yes or N for No")
                next_round = input().upper().strip()
                if next_round == "Y" or next_round == "N":
                    break
                else:
                    print ("Invalid input, please type Y or N only")
            if next_round == "Y":
               player["health"] = 10
               player["inventory"] = []
            else:
               # print high score round
               print_high_score_round(high_score_round)
               break
        print (f"Game over {player["name"]}! THANK YOU for playing.. see you next time!")
        


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    all_rounds = create_all_rounds()
    high_score_round = create_high_score_round()
    run_game_loop(player, treasures, all_rounds, high_score_round )

if __name__ == "__main__":
    main()
