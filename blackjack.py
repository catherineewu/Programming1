# LISTS AND KEPT INFO
import p1_random as p1
rng = p1.P1Random()
card_names = [0, 'ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
card_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# STARTING VALUES
current_game = 1
player_wins, dealer_wins, ties = 0, 0, 0
keep_playing = True
special = 'none'
post_statistics = False
'''
for index in range(1,14):
    print(f'{card_names[index]} has value {card_values[index]}')
'''

# GAME START
while keep_playing:
    print(f'START GAME #{current_game}\n')
    player_hand = 0
    continue_turn = True
    while continue_turn:
        if not post_statistics:
            draw = rng.next_int(13) + 1
            if draw <= 10:
                card_value = draw
            else:
                card_value = 10
            player_hand = player_hand + card_value
            if player_hand == 21:
                continue_turn = False
                special = 'BLACKJACK'
            if player_hand > 21:
                continue_turn = False
                special = 'over 21'
            print(f'Your card is a {card_names[draw]}!')
            print(f'Your hand is: {player_hand}')
        else:
            post_statistics = False
        if special != 'none':
            break
        print('''
1. Get another card
2. Hold hand
3. Print statistics
4. Exit
''')
        menu_select = int(input('Choose an option: '))
        print()
        if menu_select == 1:
            continue
        elif menu_select == 2:
            special = 'end turn'
            break
        elif menu_select == 3:
            print('Number of Player wins:', player_wins)
            print('Number of Dealer wins:', dealer_wins)
            print('Number of tie games:', ties)
            print('Total # of games played is:', current_game - 1)
            print('Percentage of Player wins:', f'{(100 * (player_wins / (current_game - 1))):.1f}', end='%\n')
            post_statistics = True
            continue
        elif menu_select == 4:
            continue_turn = False
            keep_playing = False
            break
        else:
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.')
            post_statistics = True
            continue
    if not keep_playing:
        break
    if special == 'BLACKJACK':
        player_wins = player_wins + 1
        print('BLACKJACK! You win!\n')
        special = 'none'
    elif special == 'over 21':
        print('\nYou exceeded 21! You lose.\n')
        dealer_wins = dealer_wins + 1
        special = 'none'
    elif special == 'end turn':
        dealer_hand = rng.next_int(11) + 16
        print(f'Dealer\'s hand: {dealer_hand}')
        print(f'Your hand is: {player_hand}\n')
        if (player_hand > dealer_hand) or (dealer_hand > 21):
            player_wins = player_wins + 1
            print('You win!\n')
        elif player_hand < dealer_hand <= 21:
            dealer_wins = dealer_wins + 1
            print('Dealer wins!\n')
        elif player_hand == dealer_hand:
            ties = ties + 1
            print('It\'s a tie! No one wins!\n')
        special = 'none'
    current_game = current_game + 1
