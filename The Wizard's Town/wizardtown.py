import json

while True:

    # *main menu*

    print("============================")
    print("     The Wizard's Town")
    print("============================")
    print("1) New Game")
    print("2) Continue")
    print("3) Exit")

    # *menu choosing*

    try:
        user_menu = int(input("Choose one of the above: "))
    except ValueError:
        print("Please type a number.")
    else:
        if user_menu == 1:
            character = input("Give me your hero's name: ")
            player = {
                "name": character,
                "level": 1,
                "health": 100,
                "coins": 0,
                "inventory": ["wooden sword", "shield"],
                "quests done": [],
                "score": 0
            }
            with open("./json/player_stats.json", "w") as file:
                json.dump(player, file)

            with open("./saves/activity.txt", "w") as file:
                file.write(" ")
            print(f"Character, {player["name"]} has been made!")

        elif user_menu == 2:
            with open("./json/player_stats.json", "r") as file:
                player = json.load(file)
            print(f"Welcome back, {player["name"]}!")
            print(f"Level:{player["level"]}")
            print(f"❤️ Health: {player["health"]}")
            print(f"🪙 Coins: {player["coins"]}")
            print(f"⭐ Score: {player["score"]}")

            # *player menu*

            while True:
                print("============================")
                print("         Main Menu")
                print("============================")
                print("1) View Character")
                print("2) Add Item")
                print("3) Complete Quest")
                print("4) Earn Health")
                print("5) Save Game")
                print("6) View Activity Log")
                print("7) Exit")

                try:
                    user_play_menu = int(input("Choose One."))
                except ValueError:
                    print("Enter a number.")
                else:
                    if user_play_menu == 1:
                        print(f"⚔️ {player["name"]} ")
                        print(f"Level: {player["level"]}")
                        print(f"❤️ Health: {player["health"]}")
                        print(f"🪙 Coins: {player["coins"]}")
                        print(f"⭐ Score: {player["score"]}")
                        print("Inventory:")

                        for item in player["inventory"]:
                            print(" -" + item + "\t")

                        with open("./saves/activity.txt", "a") as file:
                            file.write("Player checked character." + "\n")

                    elif user_play_menu == 2:
                        print("============================")
                        print("             Shop")
                        print("============================")
                        print("Items:")
                        print("1. 🥛 Milk: 100🪙")
                        print("2. 🐈 Pet cat: 500🪙")
                        print("3. 🐕 Pet dog: 500🪙")

                        try:
                            user_shop = int(input("Choose one if you want it. "))
                        except ValueError:
                            print("Enter one of 1,2,3.")
                        else:
                            with open("./saves/activity.txt", "a") as file:
                                file.write("Player opened shop." + "\n")

                            if user_shop == 1 and player["coins"] >= 100:
                                print("Milk Added.")
                                player["coins"] = player["coins"] - 100
                                print(f"Amount of coins left: {player["coins"]}")
                                player["inventory"].append("milk")

                                with open("./saves/activity.txt", "a") as file:
                                    file.write("Player bought milk." + "\n")

                            elif user_shop == 2 and player["coins"] >= 500:
                                print("Cat Added.")
                                player["coins"] = player["coins"] - 500
                                print(f"Amount of coins left: {player["coins"]}")
                                player["inventory"].append("cat")

                                with open("./saves/activity.txt", "a") as file:
                                    file.write("Player bought a pet cat." + "\n")

                            elif user_shop == 3 and player["coins"] >= 500:
                                print("Dog Added.")
                                player["coins"] = player["coins"] - 500
                                print(f"Amount of coins left: {player["coins"]}")
                                player["inventory"].append("dog")

                                with open("./saves/activity.txt", "a") as file:
                                    file.write("Player bought a pet dog." + "\n")

                            elif user_shop == 1 and player["coins"] < 100:
                                print("❌ Not enough coins!")

                            elif user_shop == 2 and player["coins"] < 500:
                                print("❌ Not enough coins!")

                            elif user_shop == 3 and player["coins"] < 500:
                                print("❌ Not enough coins!")

                            else:
                                print("PLease type one of 1, 2, 3.")

                    elif user_play_menu == 3:
                        while True:
                            print("========================")
                            print("The Village of quests!")
                            print("========================")
                            print("1) Baby lion (50 coins)")
                            print("2) The Egg of Secrets (100 coins)")
                            print("3) Dragon's attack (150 coins)")
                            print("4) Warriors, GO! (200 coins)")
                            print("5) The Final One... (250 coins)")
                            print("6) Exit")

                            with open("./saves/activity.txt", "a") as file:
                                file.write("Player has wanted to do a quest ." + "\n")

                            try:
                                user_quest = int(input("Choose:"))
                            except ValueError:
                                print("Enter a valid number.")
                            else:
                                if user_quest == 1:
                                    user_quest1 = input("What is 2 + 2? ")

                                    if user_quest1 == "4":
                                        print("Correct! ✅")
                                        player["coins"] = player["coins"] + 50
                                        player["score"] = player["score"] + 100
                                        print(f"Coins: {player["coins"]}")
                                        print(f"Score: {player["score"]}")
                                        player["quests done"].append("Baby lion")

                                        with open("./saves/activity.txt", "a") as file:
                                            file.write("Player finished (Baby lion)." + "\n")
                                    else:
                                        print("Wrong! ❌")
                                        player["health"] = max(player["health"] - 10, 0)
                                        print(f"Lives: {player["health"]}")

                                elif user_quest == 2:
                                    user_quest2 = input("What is 45 + 43? ")

                                    if user_quest2 == "88":
                                        print("Correct! ✅")
                                        player["coins"] = player["coins"] + 100
                                        player["score"] = player["score"] + 250
                                        print(f"Coins: {player["coins"]}")
                                        print(f"Score: {player["score"]}")
                                        player["quests done"].append("The Egg of Secrets")

                                        with open("./saves/activity.txt", "a") as file:
                                            file.write("Player finished (The Egg of Secrets)." + "\n")
                                    else:
                                        print("Wrong! ❌")
                                        player["health"] = max(player["health"] - 10, 0)
                                        print(f"Lives: {player["health"]}")

                                elif user_quest == 3:
                                    user_quest3 = input("What is 43 * 3? ")

                                    if user_quest3 == "129":
                                        print("Correct! ✅")
                                        player["coins"] = player["coins"] + 150
                                        player["score"] = player["score"] + 500
                                        print(f"Coins: {player["coins"]}")
                                        print(f"Score: {player["score"]}")
                                        player["quests done"].append("Dragon's attack")

                                        with open("./saves/activity.txt", "a") as file:
                                            file.write("Player finished (Dragon's attack)." + "\n")
                                    else:
                                        print("Wrong! ❌")
                                        player["health"] = max(player["health"] - 10, 0)
                                        print(f"Lives: {player["health"]}")

                                elif user_quest == 4:
                                    user_quest4 = input("What is (2^3)*(35*54)? ")

                                    if user_quest4 == "15120":
                                        print("Correct! ✅")
                                        player["coins"] = player["coins"] + 200
                                        player["score"] = player["score"] + 750
                                        print(f"Coins: {player["coins"]}")
                                        print(f"Score: {player["score"]}")
                                        player["quests done"].append("Warriors, GO!")

                                        with open("./saves/activity.txt", "a") as file:
                                            file.write("Player finished (Warriors, GO!)." + "\n")
                                    else:
                                        print("Wrong! ❌")
                                        player["health"] = max(player["health"] - 10, 0)
                                        print(f"Lives: {player["health"]}")

                                elif user_quest == 5:
                                    user_quest5 = input("x + y + z = ? ")

                                    if user_quest5 == 6:
                                        print("Correct! ✅")
                                        player["coins"] = player["coins"] + 250
                                        player["score"] = player["score"] + 1000
                                        print(f"Coins: {player["coins"]}")
                                        print(f"Score: {player["score"]}")
                                        player["quests done"].append("The Final One...")

                                        with open("./saves/activity.txt", "a") as file:
                                            file.write("Player finished (The Final One...)." + "\n")
                                    else:
                                        print("Wrong! ❌")
                                        player["health"] = max(player["health"] - 10, 0)
                                        print(f"Lives: {player["health"]}")

                                elif user_quest == 6:
                                    break

                                else:
                                    print("Enter 1,2,3,4,5,6 please.")

                    elif user_play_menu == 4:
                        user_healths = input("Which animal has the same fingerprints as humans? ")

                        if user_healths == "koala":
                            print("Correct! ✅")
                            player["health"] = min(player["health"] + 10, 100)
                        else:
                            print("Wrong! ❌")
                            print("Better Luck next time!")

                    elif user_play_menu == 5:
                        with open("./json/player_stats.json", "w") as file:
                            json.dump(player, file, indent=4)

                            with open("./saves/activity.txt", "a") as file:
                                file.write("Player Saved." + "\n")

                            print("🗃️ Game saved!")

                    elif user_play_menu == 6:
                        with open("./saves/activity.txt", "r") as file:
                            activity = file.read()
                            print("Activity log:")
                            print(activity)

                    elif user_play_menu == 7:
                        break

        elif user_menu == 3:
            break

        else:
            print("Please type one of 1,2,3.")