def birthday_event(player):
    # Get the player's birthday.
    birthday = player.get_birthday()

    # Get the player's heart level with the NPC.
    heart_level = player.get_heart_level_with(npc)

    # Choose a gift based on the player's heart level.
    if heart_level == 0:
        gift = "Nothing"
    elif heart_level == 1:
        gift = "A flower"
    elif heart_level == 2:
        gift = "A piece of fruit"
    elif heart_level == 3:
        gift = "A cooked meal"
    elif heart_level == 4:
        gift = "A piece of jewelry"
    elif heart_level == 5:
        gift = "A pet"

    # Give the gift to the NPC.
    give_gift(player, npc, gift)

    # Say happy birthday to the NPC.
    npc.say_happy_birthday()

    # Check if the player has any friends.
    friends = player.get_friends()

    # If the player has any friends, send them a letter.
    if friends:
        for friend in friends:
            letter = "Happy birthday, [friend.name]! I hope you have a wonderful day."
            player.send_letter(friend, letter)

    # Check if the player has any family members.
    family = player.get_family()

    # If the player has any family members, visit them.
    if family:
        for family_member in family:
            player.visit_house(family_member)

    # Add the birthday event to the game.
    game.add_event("birthday_event", birthday_event)
