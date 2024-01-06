def sum(lst):
    return lst[0] + lst[1] + lst[2]

def check_win(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [0, 3, 6], [2, 5, 8]]
    for win in wins:
        if sum(xState[win[0]:win[2] + 1]) == 3:
            print("X is the Winner")
            return 1
        if sum(zState[win[0]:win[2] + 1]) == 3:
            print("0 is the Winner")
            return 0
    else:
        return -1

def printboard(xState , zState):
    zero = 'X' if xState[0] else ('0' if zState[0] else 0)
    one = 'X' if xState[1] else ('0' if zState[1] else 1)
    two = 'X' if xState[2] else ('0' if zState[2] else 2)
    three = 'X' if xState[3] else ('0' if zState[3] else 3)
    four = 'X' if xState[4] else ('0' if zState[4] else 4)
    five = 'X' if xState[5] else ('0' if zState[5] else 5)
    six = 'X' if xState[6] else ('0' if zState[6] else 6)
    seven = 'X' if xState[7] else ('0' if zState[7] else 7)
    eight = 'X' if xState[8] else ('0' if zState[8] else 8)
    print(f"| {zero} | {one} | {two} |")

    print(f"| {three} | {four} | {five} |")

    print(f"| {six} | {seven} | {eight} |")







if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while True:
        printboard(xState, zState)
        if turn == 1:
            print("Its X's chance")
            value = int(input("Please enter a value"))
            xState[value] = 1
        else:
            print("Its 0's chance")
            value = int(input("Please enter a value"))
            zState[value] = 1
            cwin = check_win(xState, zState)

            if cwin!=-1:
                printboard(xState, zState)
                break
        turn = 1 - turn


