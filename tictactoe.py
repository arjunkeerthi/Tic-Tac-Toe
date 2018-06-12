from random import randint;
import time;
import sys;

def displayBoard(board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']) :
    print(f'\n\n             |   |                      |   |');
    print(f'           1 | 2 | 3                  {board[0]} | {board[1]} | {board[2]}');
    print(f'             |   |                      |   |');
    print(f'          -----------                -----------');
    print(f'             |   |                      |   |');
    print(f'           4 | 5 | 6                  {board[3]} | {board[4]} | {board[5]}');
    print(f'             |   |                      |   |');
    print(f'          -----------                -----------');
    print(f'             |   |                      |   |');
    print(f'           7 | 8 | 9                  {board[6]} | {board[7]} | {board[8]}');
    print(f'             |   |                      |   |\n\n');


def chooseFirst() :
    return randint(0,1);
    
    
def getPieceSelection(first) :
    dispStrSlow(f'Player {first}, please select your piece (\'X\' or \'O\'): ', 0.05);
    choice = input().upper();
    while choice != 'X' and choice != 'O' :
        if choice == '-1' : sys.exit();
        dispStrSlow('Please enter either \'X\' or \'O\': ', 0.05);
        choice = input().upper();
    
    if first == 1 :
        if choice == 'X' :
            return (choice, 'O');
        else :
            return (choice, 'X');
    else :
        if choice == 'X' :
            return ('O', choice);
        else :
            return ('X', choice);

            
def getMove(player, board) :
    validNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    move = input(f'Player {player}, pick the spot for your next move (or -1 to exit): ');
    
    open = False;
    if move.isdigit() :
        open = isOpen(int(move)-1, board)
    while not open :
        if move == '-1' : sys.exit('\n\nGoodbye!');
        msg = 'Please pick a valid spot (number from 1 to 9 or -1 to exit): ';
        if move in validNums : msg = 'That spot is already taken! Choose an open spot (or -1 to exit): ';
        move = input(msg);
        if move.isdigit() :
            open = isOpen(int(move)-1, board)
    else : 
        move = int(move);
        
    return move;


def isOpen(location, board) :
    try:
        return board[location].isspace();
    except:
        return False;
    
    
def updateBoard(move, board, piece) :
    board[move-1] = piece;


def toggle(turn) :
    if turn == 0 :
        return 1;
    else :
        return 0;
 

def checkWin(board) :
    #converts between 2D coordinates, where x increases from left (0) to right(2) 
    #and y from top (0) to bottom (2), to the indexes in the board list (index = x+3y)
    def convertToIndex(coordinate) : return coordinate[0] + 3*coordinate[1];
    
    def checkStreak(start, xStep, yStep) : 
        streak = 0;
        x = start[0];
        y = start[1];
        while streak < 3 and x < 3 and y < 3 :
            if board[convertToIndex(start)].isspace() : return False;
            if board[convertToIndex((x,y))] == board[convertToIndex(start)] :
                streak +=1;
            else :
                return False;
            x += xStep;
            y += yStep;
        return streak == 3;
        
    #For bigger grids, 3 could be replaced with new size
    values = [x for x in range(1, 3)]
    zeroes = [0]*3;
    points1 = list(zip(values, zeroes));
    points2 = list(zip(zeroes, values));
    #All possible winning combinations must include the top row and left column
    possibleStarts = points1 + points2;
    
    win = False;
    for t in possibleStarts :
        if t[0] == 0 :
            win = checkStreak(t, 1, 0);
        else :
            win = checkStreak(t, 0, 1);
        if win :
            return True;
    
    #Checks for (0,0) and diagonal from (2,0)
    return checkStreak((0,0), 1, 0) or checkStreak((0,0), 0, 1) or checkStreak((0,0), 1, 1) or checkStreak((2,0), -1, 1); 
    
    
def checkTie(board) :
    return ' ' not in board;
    
    
def getReplay() :
    dispStrSlow('\n\nDo you want to play again (Y or N)?', 0.05);
    askReplay = input().upper();
    while askReplay != 'Y' and askReplay != 'N' :
        dispStrSlow('Enter either \'Y\' or \'N\'?', 0.05);
        askReplay = input().upper();
    print('\n');
    return askReplay;
    

def displayInstructions(speed) :
    dispStrSlow('\nInstructions: Y\'all know how to play tic-tac-toe: get three of your pieces in a row \n(either along a column, row, or diagonal), and you win.\n', speed);
    dispStrSlow('To enter your moves, enter the number corresponding to the spot you want to play according \nto the diagram on the left below (which will be displayed every turn so you won\'t forget)\n', speed);
    time.sleep(0.3);
    displayBoard();
    time.sleep(0.3);
    dispStrSlow('If you ever want to exit the game, type \'-1\' to exit.\n', speed);
    dispStrSlow('Got it? Great! Now, decide amongst yourselves who will be Player 1 and Player 2.\n', speed);
    time.sleep(1);
    dispStrSlow('Ready? ', speed);
    time.sleep(1);
    dispStrSlow('Type anything to get started!', speed)
    input();
    print();


def displayStatistics(players, total) :
    p1 = players[0][2];
    p2 = players[1][2];
    
    perc1 = (p1/total)*100;
    perc2 = (p2/total)*100;
    
    print('------------------------------------------------------------------------------------');
    dispStrSlow(f'End game stats: \n', 0.05);
    dispStrSlow(f'Number of games played: {total}\n', 0.05);
    dispStrSlow(f'Number of games won: Player 1 -> {p1}, Player 2 -> {p2}\n', 0.05);
    dispStrSlow(f'Winning percentages: Player 1 - {perc1:1.1f}%, Player 2 - {perc2:1.1f}%\n', 0.05);
    print('------------------------------------------------------------------------------------');
 

def dispStrSlow(phrase, t) :
    for i in phrase :
        print(i, end='');
        sys.stdout.flush();
        time.sleep(t);
 
    
def main() :
    players = [[1, ' ', 0], [2, ' ', 0]];
    totalGames = 0;
    displayInstructions(0.03);
    replay = True;
    while replay :
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];

        first = chooseFirst();
        
        dispStrSlow('The person going first will be ', 0.03);
        dispStrSlow('...', 0.5); 
        dispStrSlow(f' Player {players[first][0]}!\n\n', 0.03); 
        time.sleep(0.5);
        print();
        
        players[0][1], players[1][1] = getPieceSelection(players[first][0]);
        dispStrSlow(f'Player 1 will be \'{players[0][1]}\' and Player 2 will be \'{players[1][1]}\'.\n\n', 0.03);
        dispStrSlow('Let\'s begin!', 0.03);
        time.sleep(1);
        displayBoard(board);
        
        gameOver = False;
        tie = False;
        currPlayer = players[first][0];
        while not gameOver and not tie:
            time.sleep(0.2);
            move = getMove(currPlayer, board);
            time.sleep(0.2);
            updateBoard(move, board, players[first][1]);
            displayBoard(board);
            gameOver = checkWin(board);
            tie = checkTie(board);
            first = toggle(first);
            currPlayer = players[first][0];
        
        if gameOver :
            dispStrSlow(f'Player {players[toggle(first)][0]} wins!', 0.03);
            players[toggle(first)][2] += 1;
        elif tie :
            dispStrSlow('It\'s a tie!', 0.03);
        
        totalGames += 1;
        replay = getReplay() == 'Y';
    
    displayStatistics(players, totalGames);
    dispStrSlow('\n\nGoodbye!\n\n', 0.03);
    
if __name__ == '__main__' :
    main();
