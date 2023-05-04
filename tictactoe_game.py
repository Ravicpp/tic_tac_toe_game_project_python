def sum(a,b,c):
    return a + b+ c


def printBoard(xState, zState):
    zero = 'x' if xState[0] else ('0' if zState[0] else 0)
    one = 'x' if xState[1] else ('0' if zState[1] else 1)
    two = 'x' if xState[2] else ('0' if zState[2] else 2)
    three = 'x' if xState[3] else ('0' if zState[3] else 3)
    four = 'x' if xState[4] else ('0' if zState[4] else 4)
    five = 'x' if xState[5] else ('0' if zState[5] else 5)
    six = 'x' if xState[6] else ('0' if zState[6] else 6)
    seven = 'x' if xState[7] else ('0' if zState[7] else 7)
    eight = 'x' if xState[8] else ('0' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkWin(xState,zState):
    Wins =[[0, 1, 2],[3, 4, 5],[6, 7, 8],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for Win in Wins:
        if(sum(xState[Win[0]],xState[Win[1]], xState[Win[2]]) == 3):
         print("x Won the match") 
         return 1
        if(sum(zState[Win[0]],zState[Win[1]], zState[Win[2]]) == 3):
          print("0 Won the match")
          return 0
    return -1    
    
xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
turn = 1 # 1 for x and 0 fro o
print("Welcome to Tic Tac Toe")
while(True):
    printBoard(xState, zState)
    if(turn == 1):
       print("x's Chance")
       value = int(input("Please enter a value : "))
       xState[value] = 1
    else:
        print("0's Chance")
        value = int(input("please enter value : "))
        zState[value] = 1
    cWin = checkWin(xState, zState)
    if(cWin!=-1):
        print("match over")
        break
    turn = 1 - turn
 
