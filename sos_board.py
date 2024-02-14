class SosBoard:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [[' ' for _ in range(col)] for _ in range(row)]
        self.board[0][0] = 'S'
        self.board[0][col-1] = 'S'
        self.board[row-1][0] = 'S'
        self.board[row-1][col-1] = 'S'
    
    def print_board(self):
        for _ in self.board:
            print(_)
    
    def show_status(self, player_1, player_2):
        self.print_board()
        player_1.print_score()
        player_2.print_score()
        print("\n")        
    
    def update_board(self, move):
        self.board[move[0]][move[1]] = move[2]
        return self.board
    
    def evaluate(self, player_one_score, player_two_score):
        return player_one_score - player_two_score

    def check_move(self, move):
        if move[0] > self.row or move[0] < 0 or move[1] > self.col or move[1] < 0:
            print('Invalid move')
            return False
        elif self.board[move[0]][move[1]] != ' ':
            print('That cell is not empty')
            return False
        else:
            return True
    
    def is_full(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == ' ':
                    return False
        return True
    
    def get_available_moves(self):
        available_moves = []
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == ' ':
                    available_moves.append([i, j, 'S'])
                    available_moves.append([i, j, 'O'])
        return available_moves
    
    def undo_move(self, move):
        self.board[move[0]][move[1]] = ' '
        return self.board
    
    def check_sos(self, move, player):
        move_row = move[0]
        move_col = move[1]
        move_letter = move[2]
        
        sos_count = 0
        
        if move_letter == 'O':
            # check row : 'SOS'
            if (move_col >= 1 and move_col <= self.col - 2) and self.board[move_row][move_col - 1] == 'S' and self.board[move_row][move_col + 1] == 'S':
                sos_count += 1
            # check column: 'SOS'
            if (move_row >= 1 and move_row <= self.row - 2) and self.board[move_row - 1][move_col] == 'S' and self.board[move_row + 1][move_col] == 'S':
                sos_count += 1
            # check diagonally top left to bottom right: 'SOS'
            if (move_row >= 1 and move_col >= 1 and move_row <= self.row - 2 and move_col <= self.col - 2) and self.board[move_row - 1][move_col - 1] == 'S' and self.board[move_row + 1][move_col + 1] == 'S':
                sos_count += 1
            # check diagonally top right to bottom left: 'SOS'
            if (move_row >= 1 and move_row <= self.row - 2 and move_col >= 1 and move_col <= self.col - 2) and self.board[move_row - 1][move_col + 1] == 'S' and self.board[move_row + 1][move_col - 1] == 'S':
                sos_count += 1
        elif move_letter == 'S':
            # check 2 left: 'SOS'
            if move_col >= 2 and self.board[move_row][move_col - 1] == 'O' and self.board[move_row][move_col - 2] == 'S':
                sos_count += 1
            # check 2 right: 'SOS'
            if move_col <= self.col -3 and self.board[move_row][move_col + 1] == 'O' and self.board[move_row][move_col + 2] == 'S':
                sos_count += 1
            # check 2 up: 'SOS'
            if move_row >= 2 and self.board[move_row - 1][move_col] == 'O' and self.board[move_row - 2][move_col] == 'S':
                sos_count += 1
            # check 2 down: 'SOS'
            if move_row <= self.row - 3 and self.board[move_row + 1][move_col] == 'O' and self.board[move_row + 2][move_col] == 'S':
                sos_count += 1
            # check diagonally bottom right S to top left: 'SOS'
            if move_row >= 2 and move_col >= 2 and self.board[move_row - 1][move_col - 1] == 'O' and self.board[move_row - 2][move_col - 2] == 'S':
                sos_count += 1
            # check diagonally bottom left S to top right: 'SOS'
            if move_row >= 2 and move_col <= self.col - 3 and self.board[move_row - 1][move_col + 1] == 'O' and self.board[move_row - 2][move_col + 2] == 'S':
                sos_count += 1
        if sos_count > 0:
            print(f'{player.nickname} scored {sos_count} SOS')
            print("\n")
            player.score += sos_count
            return True
        else:
            return False
    
    def check_minimax_sos(self, move, player_score):
        move_row = move[0]
        move_col = move[1]
        move_letter = move[2]
        
        sos_count = 0
        
        if move_letter == 'O':
            # check row : 'SOS'
            if (move_col >= 1 and move_col <= self.col - 2) and self.board[move_row][move_col - 1] == 'S' and self.board[move_row][move_col + 1] == 'S':
                sos_count += 1
            # check column: 'SOS'
            if (move_row >= 1 and move_row <= self.row - 2) and self.board[move_row - 1][move_col] == 'S' and self.board[move_row + 1][move_col] == 'S':
                sos_count += 1
            # check diagonally top left to bottom right: 'SOS'
            if (move_row >= 1 and move_col >= 1 and move_row <= self.row - 2 and move_col <= self.col - 2) and self.board[move_row - 1][move_col - 1] == 'S' and self.board[move_row + 1][move_col + 1] == 'S':
                sos_count += 1
            # check diagonally top right to bottom left: 'SOS'
            if (move_row >= 1 and move_row <= self.row - 2 and move_col >= 1 and move_col <= self.col - 2) and self.board[move_row - 1][move_col + 1] == 'S' and self.board[move_row + 1][move_col - 1] == 'S':
                sos_count += 1
        elif move_letter == 'S':
            # check 2 left: 'SOS'
            if move_col >= 2 and self.board[move_row][move_col - 1] == 'O' and self.board[move_row][move_col - 2] == 'S':
                sos_count += 1
            # check 2 right: 'SOS'
            if move_col <= self.col -3 and self.board[move_row][move_col + 1] == 'O' and self.board[move_row][move_col + 2] == 'S':
                sos_count += 1
            # check 2 up: 'SOS'
            if move_row >= 2 and self.board[move_row - 1][move_col] == 'O' and self.board[move_row - 2][move_col] == 'S':
                sos_count += 1
            # check 2 down: 'SOS'
            if move_row <= self.row - 3 and self.board[move_row + 1][move_col] == 'O' and self.board[move_row + 2][move_col] == 'S':
                sos_count += 1
            # check diagonally bottom right S to top left: 'SOS'
            if move_row >= 2 and move_col >= 2 and self.board[move_row - 1][move_col - 1] == 'O' and self.board[move_row - 2][move_col - 2] == 'S':
                sos_count += 1
            # check diagonally bottom left S to top right: 'SOS'
            if move_row >= 2 and move_col <= self.col - 3 and self.board[move_row - 1][move_col + 1] == 'O' and self.board[move_row - 2][move_col + 2] == 'S':
                sos_count += 1
        player_score += sos_count
        return player_score, sos_count