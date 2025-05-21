'''
monopoly.py
Run this file to play Monopoly Game
'''

import element
import random

def roll_dice(name: str, round_count: int, round: int) -> int:
    point = random.randint(1, 6)

    input(f'<Round: {round_count:02}/{round:02}> [{name}] please roll the dice please [Enter]')
    input(f'... ... Please Advance {point} Spaces ... ...')   
    return point

#Handle interactions when a player lands on a city.
def interact_city(map_list, player, owner):
    current_city = map_list[player.location]
    print(current_city)

    # Case 1: The city is unowned — player can buy it
    if current_city.owner == " ":
        while True:
            command = input(f'[{player.name}] Would you like to buy it? Y/N ')
            if command == 'Y':
                if player.money >= current_city.price:
                    print(f'Congratulations [{player.name}]! You own [{current_city.name}] now!')
                    player.money -= current_city.price
                    current_city.owner = player.name
                    current_city.house_number += 1
                    print(current_city)
                    input('(Press [Enter] to continue...)')
                elif player.money < current_city.price:
                    print(f'Sorry [{player.name}], You can\'t afford it\n')
                    input('(Press [Enter] to continue...)')
                break
            elif command == 'N':
                print(f'OK [{player.name}], You can have a break here.\n')
                input('(Press [Enter] to continue...)')
                break
            else:
                print(f'Hi [{player.name}], Please make a decision')

    # Case 2: The player already owns the city — player can upgrade it
    elif current_city.owner == player.name:
        while True:
            command = input(f'{current_city.name} has {current_city.house_number} house(s) now.\n [{player.name}] Would you like to upgrade it? Y/N ')

            if command == 'Y':
                if player.money >= current_city.price:
                    player.money -= current_city.price
                    current_city.house_number += 1
                    current_city.rent *= 2
                    print(f'Congratulations [{player.name}] ! {current_city.name} has {current_city.house_number} house(s) now!')           
                    print(current_city)
                    input('(Press [Enter] to continue...)')
                else:
                    print(f'Sorry [{player.name}], You can\'t afford it\n')
                    input('(Press [Enter] to continue...)')
                break
            elif command == 'N':
                print(f'OK [{player.name}], You can stay in your house\n')
                input('(Press [Enter] to continue...)')
                break
            else:
                print(f'[{player.name}], Please make a decision')

    # Case 3: The city is owned by another player — player should pay rent to the another player  
    elif current_city.owner != player.name:
        print(f'You should pay M$ {current_city.rent} rent to [{current_city.owner}]!\n')
        player.money -= current_city.rent
        owner.money += current_city.rent
        print(player)
        input('(Press [Enter] to continue...)')


# Determine if the game should end and announce the winner.
def win_or_lose(player1, player2, round_count, round) -> bool:

    if round_count >= round or player1.money <= 0 or player2.money <= 0:
        if player1.money > player2.money:
            winer = player1
            loser = player2
        elif player1.money < player2.money:
            winer = player2
            loser = player1
        else:
            print('The game ends in a draw.')
            return True
        print(f'[{winer.name}] wins! Congratulations!\n')
        print('____Game Results____')
        print(f'>>>winer: {winer.name}<<<', end = '')
        print(winer)
        input('(Press [Enter] to continue...)')
        print(f'>>>loser: {loser.name}<<<', end = '')
        print(loser)
        input('(Press [Enter] to End...)')
        return True

# Main game: initialize players, map indexs and cities, and game flow.
def main():

    round_count = 1
    while True:
        try:
            round = int(input('How many rounds do you want to play? '))
            if round > 0:
                break
        except ValueError:
                print('Please Enter an positive integer')
    # Input Player 1 name
    while True:
        player_name = input('How should I address you? Player1: ')
        player1 = element.Player(f'{player_name}')
        if player1.name != '':
            break

    # Input Player 2 name
    while True:
        player_name = input('How should I address you? Player2: ')
        player2 = element.Player(f'{player_name}')
        if player2.name != '':
            break

    # Initialize every tile attributes 
    map_list = []
    for key, value in element.map_index.items():
        map_list.append(element.City(value, 50, 40, key))
    
    while True:
        
        # Player 1 turn
        is_city = player1.action(roll_dice(player1.name, round_count, round))
        print(player1)
        input('(Press [Enter] to continue...)')
        if is_city:
            interact_city(map_list, player1, player2)

        # Player 2 turn
        is_city = player2.action(roll_dice(player2.name, round_count, round))
        print(player2)
        input('(Press [Enter] to continue...)')
        if is_city:
            interact_city(map_list, player2, player1)

        # Check game end conditions
        quit = win_or_lose(player1, player2, round_count, round)
        if quit:
            break
        round_count += 1
    
if __name__ == '__main__':
    main()

