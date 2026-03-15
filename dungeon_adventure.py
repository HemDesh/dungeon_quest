import random

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

    def display_options(room_number):
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
        print (f"You are in room number {room_number}")
        print ("What would you like to do?")
        print ("    1. Search for treasure")
        print ("    2. Move to next room")
        print ("    3. Check health and inventory")
        print ("    4. Quit the game")

    def search_room(player, treasures):
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


    def check_status(player):
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


    def end_game(player, treasures):
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
        print (f"Your final health is {player["health"]}")
        count = len(player["inventory"])
        if count > 0:
            print (f"Your total score is {total_score}")
            print ("You have gained ", end="")
            counter = 0
            for key, value in player["inventory"]:
                print (key, end="")
                counter+=1
                if len(player["inventory"]) > 1:
                    if counter+1 == len(player["inventory"]):
                        print (" & ", end="")
                    else:
                        if counter < len(player["inventory"]):
                            print (" , ", end ="")
            print (" Nice job!!")
        else:
            print ("Sorry, you did not gain any treasure")


        # TODO: End with a message like "Game Over! Thanks for playing."
        print (f"Game over {player["name"]}! THANK YOU for playing.. see you next time!")

    def run_game_loop(player, treasures):
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
        for i in range(1,6):
        # TODO: Inside each room, prompt player choice using input()
            while i > 0:
                display_options(i)
                choice = input()
        # TODO: Use if/elif to handle each choice (1–4)
                if choice >= "1" and choice <= "4":
                    if choice == "1":
                        search_room(player, treasures)
                        break
                    elif choice == "2":
                        print (f"You have skipped room number {i}")
                        break
                    elif choice == "3":
                        check_status(player)
                    else:
                        break
                else:
                    print ("Please select option between 1 and 4 only, try again!")
        # TODO: Break or return appropriately when player quits or dies
            if choice == "4" or player["health"] == 0:
                break
        # TODO: Call end_game() after all rooms are explored
        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    # search_room(player, treasures)
    # search_room(player, treasures)
    # search_room(player, treasures)
    # check_status(player)
    # end_game(player, treasures)
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
