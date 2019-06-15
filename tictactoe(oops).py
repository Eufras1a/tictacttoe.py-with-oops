from random import randint, choice
from time import sleep
def main():
    user = tictactoe()
    user.play()

class tictactoe:
    
    def __init__(self):
        self.set_board() 
        self.sym['comp'] = self.set_controller() 
    
    
    def set_board(self):
        self.board = {'top-L'    : ' ',
                      'top-M'    : ' ',
                      'top-R'    : ' ',
                      'mid-L'    : ' ',
                      'mid-M'    : ' ',
                      'mid-R'    : ' ',
                      'bottom-L' : ' ',
                      'bottom-M' : ' ',
                      'bottom-R' : ' ' }
        self.list_board = list(self.board.keys())


    def set_controller(self):
        self.sym = { 'player' : ' ', 'comp' : ' '}
        print('Would you like to play with alphabetical "X" or "O" ?')

        while True:
            self.sym['player'] = input().upper()

            if self.sym['player'] == 'X':
                return 'O'
            elif self.sym['player'] == 'O':
                return 'X'
            else:
                print('pls either enter alphabetical X or O to proced further into the game', end = ': ')

    
    def show_board(self):
        print()
        print(self.board['top-L'] + '|' + self.board['top-M'] + '|' + self.board['top-R']) 
        print('-----')
        print(self.board['mid-L'] + '|' + self.board['mid-M'] + '|' + self.board['mid-R'])
        print('-----') 
        print(self.board['bottom-L'] + '|' + self.board['bottom-M'] + '|' + self.board['bottom-R']) 
        print()
        print()

    
    def play(self):
        self.show_board()

        if randint(0, 1) == 1:
            print('Computer starts first!!')
            self.comp_move()

        while True: 
            self.player_move()
            if self.win_checker(self.sym['player']):
                break

            self.comp_move()
            if self.win_checker(self.sym['comp']):
                break
        print(self.__dict__)

    # comp move 
    def comp_move(self):
        print("It's computer's turn....")
        sleep(1)
        print('...')
        sleep(0.5)
        move = choice(self.list_board)
        self.board[move] = self.sym['comp']
        self.list_board.remove(move)
        self.show_board()

    # player move 
    def player_move(self):
        print("Where would you like to mark ? (for Row type [top-,  mid-, bottom-] and for column type [L, M, R] ) example:  top-L")

        while True:
            move = input()
            if self.board.get(move, 'Fail') == 'Fail':
                print('error: invalid keyword, try again')
            elif self.board[move] != " ":
                print('that place is already filled duh!!!')
            else:
                self.board[move] = self.sym['player']
                self.list_board.remove(move)
                break
        self.show_board()

    # win checker 
    def win_checker(self, temp):
        # check for if anyone makes a line
        if self.board['top-L'] == self.board['top-R'] == self.board['top-M'] == temp :
            return self.end_msg(temp)
        elif self.board['mid-L'] == self.board['mid-R'] == self.board['mid-M'] == temp :
            return self.end_msg(temp)
        elif self.board['bottom-L'] == self.board['bottom-R'] == self.board['bottom-M'] == temp :
            return self.end_msg(temp)
        elif self.board['top-L'] == self.board['bottom-L'] == self.board['mid-L'] == temp :
            return self.end_msg(temp)
        elif self.board['top-R'] == self.board['bottom-R'] == self.board['mid-R'] == temp :
            return self.end_msg(temp)
        elif self.board['top-M'] == self.board['bottom-M'] == self.board['mid-M'] == temp :
            return self.end_msg(temp)
        elif self.board['top-L'] == self.board['mid-M'] == self.board['bottom-R'] == temp :
            return self.end_msg(temp)
        elif self.board['top-R'] == self.board['mid-M'] == self.board['bottom-L'] == temp :
            return self.end_msg(temp)

        # if the board is filled then tie
        if not self.list_board:
            return self.end_msg('tie')

        return False


    def end_msg(self, temp):
        
        if temp == self.sym['player']:
            print('Congratulations you won!!!')
        elif temp == self.sym['comp']:
            print('Game Over')
        else:
            print()
            print("It's a tie!!!")

        return True


if __name__ == '__main__':
    while True:
        main()
        print('Would you like to play again ?', 'Press "y" to play again or to quit press any key', sep = '\n')
        if input().lower() != 'y' :
            break