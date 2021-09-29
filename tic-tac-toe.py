import random

def display_grid(grid):
    print('\n' *10)
    print("   |   |  ")
    print(" "+grid[0]+" | "+grid[1]+" | "+grid[2])
    print("   |   |  ")
    print("_____________")
    print("   |   |  ")
    print(" "+grid[3]+" | "+grid[4]+" | "+grid[5])
    print("   |   |  ")
    print("_____________")
    print("   |   |  ")
    print(" "+grid[6]+" | "+grid[7]+" | "+grid[8])
    print("   |   |  ")

def take_input(marker):
    while True:
        num=int(input("Choose a number from 1-9 "))
        print(type(num))
        if type(num)!=int:
            print("Invalid entry!Not a number.Try again.")
        elif num>9 or num<1:
            print("Invalid entry!Out of range.Try again.")
        elif grid[num-1]!=" ":
            print("Position taken.Try again.")
        else:
            grid[num-1]=marker
            print("done")
            return
def win_check(grid,marker):
    ###Row#########
    return ((grid[0]==grid[1]==grid[2]==marker) or
    (grid[3]==grid[4]==grid[5]==marker) or
    (grid[6]==grid[7]==grid[8]==marker) or

    (grid[0]==grid[3]==grid[6]==marker) or
    (grid[1]==grid[4]==grid[7]==marker) or
    (grid[2]==grid[5]==grid[8]==marker) or

    (grid[0]==grid[4]==grid[8]==marker) or
    (grid[2]==grid[4]==grid[6]==marker) )
def full_board_check(grid):
    for i in range(0,9):
        if grid[i]==" ":
            return False
    return True
def replay():
    play=input("Do you want to play again?Y/N ").upper()
    return play=="Y"

print("Welcome to Tic-tac-toe!!!")
while True:
    grid=[' ']*9
    display_grid(grid)
    Player1_cur="X"
    Player2_cur="O"

    start=input("Let's start the game?Y/N ").upper()
    if start=="Y":
        on=True
    else:
        on=False
    turn="Player 1"
    while on==True:
        if turn=="Player 1":
            marker="X"
            display_grid(grid)
            take_input(marker)
            if win_check(grid,marker):
                display_grid(grid)
                print("Player 1 won!!!")
                print("Game Over!!")
                break
            else:
                if full_board_check(grid):
                    print("Game Tied!!")
                    # print("Game Over!!")
                    break
                else:
                    turn="Player 2"
        else:
            marker="O"
            display_grid(grid)
            take_input(marker)
            if win_check(grid,marker):
                display_grid(grid)
                print("Player 2 won!!!")
                print("Game Over!!")
                break
            else:
                if full_board_check(grid):
                    print("Game Tied!!")
                    print("Game Over!!")
                    break
                else:
                    turn="Player 1"
    if not replay():
        break