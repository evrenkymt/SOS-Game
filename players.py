class Players:
    def __init__(self, nickname):
        self.nickname = nickname
        self.score = 0
    
    def print_score(self):
        print(f'{self.nickname} has {self.score} points')
    
    def get_move(self):
        move = input('Enter row column and letter: ')
        move = move.split(' ')
        move[0] = int(move[0])
        move[1] = int(move[1])
        move[2] = move[2].upper()
        return move

class AiPlayer(Players):
    def __init__(self, nickname):
        super().__init__(nickname)
    
    def get_move(self, board, depth, player_one_score, player_two_score):
        _, best_move = self.minimax(board, depth, True, player_one_score, player_two_score)
        return best_move
    
    def minimax(self, board, depth, is_maximizing, player_one_score, player_two_score):
        # Check if the game is over or the depth limit is reached
        if board.is_full() or depth == 0:
            return board.evaluate(player_one_score, player_two_score), None   

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None

            for move in board.get_available_moves():
                board.update_board(move)
                
                player_one_score, sos = board.check_minimax_sos(move, player_one_score)
                
                eval, _ = self.minimax(board, depth - 1, False, player_one_score, player_two_score)
                board.undo_move(move)
                player_one_score -= sos

                if eval > max_eval:
                    max_eval = eval
                    best_move = move

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for move in board.get_available_moves():
                board.update_board(move)
                
                player_two_score, sos = board.check_minimax_sos(move, player_two_score)
                
                eval, _ = self.minimax(board, depth - 1, True, player_one_score, player_two_score)
                board.undo_move(move)
                player_two_score -= sos
                

                if eval < min_eval:
                    min_eval = eval
                    best_move = move

            return min_eval, best_move