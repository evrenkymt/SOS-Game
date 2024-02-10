from players import Players

class AI_Players(Players):
    def __init__(self, nickname):
        super().__init__(nickname)
    
    def get_move(self):
        raise NotImplementedError('AI players dont take input from user. They make their own move.')
    
    def minimax(self, board, depth, is_maximizing):
        # check there are no more empty spaces or depth limit is reached.
        if board.is_full() or depth == 0:
            return self.evaluate(board), None
        
        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            
            for move in board.get_available_moves():
                # should be a copy of the board
                new_board = board
                new_board.update_board(move)
                
                eval, _ = self.minimax(new_board, depth - 1, False)
                
                