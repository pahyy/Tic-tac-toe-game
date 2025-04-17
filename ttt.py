scoreX=0
scoreO=0

class XO:
    def __init__(self):
        self.board = [" " for i in range(9)]
        self.player = "X"
        self.over = False

    
    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            print("--+---+--")
    
    def move(self, i):
        if(self.board[i] == " "):
            self.board[i]=self.player
            win = self.check()
            if(win):
                self.print_board()
                print(f"Player {self.player} wins!")
                if(self.player == "X"):
                    global scoreX
                    scoreX+=1
                elif(self.player == "O"):
                    global scoreO
                    scoreO+=1
                self.over=True
            elif(" " not in self.board):
                self.print_board()
                print("Its a draw")
                self.over=True
            else:
                if(self.player == "X"):
                    self.player = "O"
                elif(self.player == "O"):
                    self.player = "X"
        else:
            print("Invalid move!")
    
    def check(self):
        win = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for x in win:
            if(self.board[x[0]] == self.board[x[1]] == self.board[x[2]] != " "):
                return True    
        return False



def main():
    
    while True:
        print("")
        print("====TicTacToe====")
        print("1. Start a new game")
        print("2. How to play")
        print("3. Score")
        print("4. Quit")
        choice = input("Choose an option: ")
        if(choice == "1"):
            game = XO()
            while(not game.over):
                game.print_board()
                try:
                    choice = int(input(f"Player {game.player} move: "))
                    if(0<choice<10):
                        game.move(choice-1)
                    else:
                        print("Invalid move!")
                except ValueError:
                    print("asd")
            
        elif(choice == "2"):
            print(" 1 | 2 | 3 ")
            print("--+---+--")
            print(" 4 | 5 | 6 ")
            print("--+---+--")
            print(" 7 | 8 | 9 ")
            print("--+---+--")
            print("On your turn input a number between 1 and 9\n"
            "correspondind to the place on which you want to mark")
        elif(choice == "3"):
            global scoreX
            global scoreO
            print(f"Player X: {scoreX}")
            print(f"Player O: {scoreO}")
        elif(choice == "4" or choice == "q"):
            break

if(__name__ == "__main__"):
    main()