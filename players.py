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