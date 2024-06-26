import itertools

game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]


def game_board(game_map, player='_', row=0, col=0, just_display=False):
    
    try:
        if game_map[row][col] != '_':
            print("This position is occupied! Choose another !!")
            return game_map, False

        if not just_display:
            game_map[row][col] = player
        print("    "+"    ".join(str(i) for i in range(len(game_map))))
        for i, row in enumerate(game_map):
            print(i, row) 

    except IndexError as e:
        print("Eror : Make sure you input row/col as 0, 1 or 2", e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

    return game_map, True


def win(game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0]!='_':
            return True
        else:
            return False
        
    # horizontal winner
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner vertically !!")
            return True
            
    #vertical winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically !!")
            return True
            
    # diagonal winner
    diag1 = []
    diag2 = []
    for i, row in enumerate(game):
        diag1.append(game[i][i])
        diag2.append(game[i][-(i+1)])
    if all_same(diag1):
        print(f"Player {diag1[0]} is the winner diagonally !!")
        return True
    if all_same(diag2):
        print(f"Player {diag2[0]} is the winner diagonally !!")
        return True

    return False


play = True
while play:
    game = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]
    
    game, _ = game_board(game, just_display = True)
    game_won = False
    player_choice = itertools.cycle(['O','X'])
    moves_remaining = len(game) * len(game)

    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        moves_remaining -= 1

        while not played:
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            col_choice = int(input("What column do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, col_choice)
            
            
        if win(game):
            game_won = True
            print("**************** Game Over ****************")
            again = input("The game is over, would you like to play it again? (y,n): ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Byeeeee")
                play = False
            else:
                print("Ehhhhh...typo")
                play = False
        
        # game tied
        if moves_remaining == 0:
            print("**************** Game Tied ****************")
            again = input("The game is tied, would you like to play it again? (y,n): ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Byeeeee")
                play = False
            else:
                print("Ehhhhh...typo")
                play = False

 