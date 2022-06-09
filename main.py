import random

class Game:
    def __init__ (self):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.player_turn = True
        self.winned = False
    
    def print_board (self):
        for row in self.board:
            print(row[0], row[1], row[2])

        print('')

    def play (self):
        row = input('Enter a row: ')
        col = input('Enter a col: ')

        row = int(row)
        col = int(col)

        if self.board[row][col] != 'x' and self.board[row][col] != 'o':
            self.board[row][col] = 'x'
            self.print_board()
        else:
            print('Position already used')
            self.play()

    def pc_play (self):
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)

        if self.board[row][col] != 'x' and self.board[row][col] != 'o':
            self.board[row][col] = 'o'
            self.print_board()
        else:
            self.pc_play()

    def toggle_turn (self):
        if self.player_turn == True:
            self.player_turn = False
        else:
            self.player_turn = True

    def check_for_empty_positions (self):
        empty_positions = False

        for row in self.board:
            for col in row:
                if col == '_':
                    empty_positions = True

        return empty_positions

    def check_win (self):
        winning_positions = [
            # Horizontal
            '00-01-02',
            '10-11-12',
            '20-21-22',

            #Vertical
            '00-10-20',
            '01-11-21',
            '02-12-22',
                
            # Diagonal
            '00-11-22',
            '02-11-20'
        ]

        for w_position in winning_positions:
            position = w_position.split('-')
            player_win = 0
            pc_win = 0

            for cell in position:
                row = int(cell[0])
                col = int(cell[1])

                if self.board[row][col] == 'x':
                    player_win += 1
                elif self.board[row][col] == 'o':
                    pc_win += 1

            if player_win == 3:
                print('Player winned!')
                self.winned = True
            elif pc_win == 3:
                print('PC winned!')
                self.winned = True

    def run (self):
        if self.check_for_empty_positions() == True and self.winned == False:
            if self.player_turn == True:
                print('Your turn')
                self.play()
            else:
                print('PC turn:')
                self.pc_play()
            
            self.check_win()
            self.toggle_turn()


game = Game()

for i in range(10):
    game.run()
