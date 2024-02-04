import sos_board
import players

class sos_game_start:
    size = input('Welcome to SOS game. Please enter row and column size:')
    row = int(size.split(' ')[0])
    col = int(size.split(' ')[1])
    
    board = sos_board.SOS_BOARD(row, col)

    player_1 = players.Players('Player 1')
    player_2 = players.Players('Player 2')

    player_turn = player_1

    board.print_board()

    i = 0
    num_of_moves = row * col - 4
    while i < num_of_moves:
        
        move = player_turn.get_move()
        while not board.check_move(move):
            move = player_turn.get_move()
        board.update_board(move)
        board.check_sos(move, player_turn)
        
        player_1.print_score()
        player_2.print_score()
        board.print_board()
        
        if player_turn == player_1:
            player_turn = player_2
        else:
            player_turn = player_1
        
        i += 1