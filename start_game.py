import sos_board
from players import Players, AiPlayer

class StartGame:
    def __init__(self):
        size = input('Welcome to SOS game. Please enter row and column size:')
        row = int(size.split(' ')[0])
        col = int(size.split(' ')[1])
    
        board = sos_board.SosBoard(row, col)
        board.print_board()

    

class AivsAiGame(StartGame):
    def __init__(self):
        super().__init__()
    
    def play_game(self, board):
        player_1 = AiPlayer('Player 1')
        player_2 = AiPlayer('AI Player 1')
    
        player_list = [player_1, player_2]
        player_turn_index = 0
    
        i = 0
        num_of_moves = 21 # duzenlencek
        while i < num_of_moves:
        
            print("\n")
            if player_turn_index == 0:
                print(f'Player 1 is making a move:')
                move = player_1.get_move(board, 4, player_1.score, player_2.score)

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

class HumanvsAiGame(StartGame):
    def __init__(self):
        super().__init__()
    
    def play_game(self, board):
        player_1 = Players('Player 1')
        player_2 = AiPlayer('AI Player 1')
    
        player_list = [player_1, player_2]
        player_turn_index = 0
    
        i = 0
        num_of_moves = 21
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

class HumanvsHumanGame(StartGame):
    def __init__(self):
        super().__init__()
    
    def play_game(self, board):
        player_1 = Players('Player 1')
        player_2 = Players('Player 2')

        player_turn = player_1

        board.print_board()

        i = 0
        num_of_moves = 21
        while i < num_of_moves:
        
            move = player_turn.get_move()
            while not board.check_move(move):
                move = player_turn.get_move()
            board.update_board(move)
            board.check_sos(move, player_turn)

            board.show_status(player_1, player_2)
        
            if player_turn == player_1:
                player_turn = player_2
            else:
                player_turn = player_1
            i += 1