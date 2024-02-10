import sos_board
from players import Players
from ai_player import AI_Players

class start_game:
    size = input('Welcome to SOS game. Please enter row and column size:')
    row = int(size.split(' ')[0])
    col = int(size.split(' ')[1])
    
    board = sos_board.SOS_BOARD(row, col)
    
    player_1 = Players('Player 1')
    player_2 = AI_Players('AI Player 1')
    
    player_list = [player_1, player_2]
    player_turn_index = 0
    
    board.print_board()
    
    i = 0
    num_of_moves = row * col - 4
    while i < num_of_moves:
        
        current_player = player_list[player_turn_index]
        
        if player_turn_index == 0:
            move = current_player.get_move()
        elif player_turn_index == 1:
            print('AI Player 1 is making a move')
            move = current_player.get_best_move(board, 2)
        
        board.update_board(move)
        board.check_sos(move, current_player)
        
        board.show_status(player_1, player_2)
        
        player_turn_index = (player_turn_index + 1) % len(player_list)
        
        i += 1