import sos_board
from players import Players
from ai_player import AiPlayer

class StartGame:
    size = input('Welcome to SOS game. Please enter row and column size:')
    row = int(size.split(' ')[0])
    col = int(size.split(' ')[1])
    
    board = sos_board.SosBoard(row, col)
    
    player_1 = Players('Player 1')
    player_2 = AiPlayer('AI Player 1')
    
    player_list = [player_1, player_2]
    player_turn_index = 0
    
    board.print_board()
    
    i = 0
    num_of_moves = row * col - 4
    while i < num_of_moves:
        
        print("\n")
        if player_turn_index == 0:
            print(f'Player 1 is making a move:')
            move = player_1.get_move()
            while not board.check_move(move):
                move = player_1.get_move()

        elif player_turn_index == 1:
            print('AI Player 1 is making a move')
            move = player_2.get_move(board, 4, player_1.score, player_2.score)
        else:
            print("Error")
        
        board.update_board(move)
        board.check_sos(move,player_list[player_turn_index])
        
        board.show_status(player_1, player_2)
        
        player_turn_index = (player_turn_index + 1) % 2
        
        i += 1