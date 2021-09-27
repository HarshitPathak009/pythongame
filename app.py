import time
import os


from test_cases import cases as case
from const import BLUE, RED, TEAM_BLUE, TEAM_RED, ARCHER_COST, TROOP_COST, CANNON_COST


class Characteristics:
    def __init__(self, *features):
        print(features)
        self.damage = features[0]
        self.attackSpeed = features[1]
        print(features)


# class Troop(Characteristics):
#     def __init__(self, *p):
#         print(p)
#         self.x = p[0]
#         self.y = p[1]
#         Characteristics.__init__(p)
    
#     #attack
#     def attack(self):
#         block = 1

        
#     #move

#     #health

#     #destroy


# class Cannon(Characteristics):
#     def __init__(self, *p):
#         print(p)
#         self.x = p[0]
#         self.y = p[1]
#         Characteristics.__init__(p)
    
#     #attack
#     def attack():
#         block = 1
        
#     #move

#     #health

#     #destroy


class Archer(Characteristics):
    def __init__(self, *p):
        print(p)
        self.x = p[0]
        self.y = p[1]
        self.color = p[2]
        self.cost = ARCHER_COST
        # Characteristics.__init__(p)
    
    #attack
    def attack():
        block = 1
        
    #move
    def move(self,board):
        if(self.color == BLUE):
            distance = 1
        else:
            distance = -1
        if((self.y+distance<8 and self.y+distance>=0) and board[self.x][self.y+distance]==0):
            board[self.x][self.y] = 0
            board[self.x][self.y+distance] = self
            self.y = self.y+distance
            

    #health

    #destroy

def print_board(board):
    for i in range(8):
        for j in range(8):
            if(board[i][j]!=0):
                print(board[i][j].cost,end="\t")
                continue
            print(board[i][j],end="\t")
        print("")

def is_correct_board(board):
    cost = 0

    #left-side cost
    for i in range(len(board)):
        for j in range(len(board)//2):
            if(board[i][j]!=0):
                cost+=board[i][j].cost
    # print(cost)
    if(cost!=100):
        return False

    #right-side cost
    cost = 0
    for i in range(len(board)):
        for j in range((len(board)//2), len(board)):
            if(board[i][j]!=0):
                cost+=board[i][j].cost
    # print(cost)
    if(cost!=100):
        return False
    

    return True

def set_board(board):
    #set Team Blue
    cost = 0
    print("Team Blue")
    while(True):
        x, y = map(int,input("Enter the position of character").strip().split())
        if(y<=3 and board[x][y]==0 and cost+ARCHER_COST<=TEAM_BLUE):
            a = Archer(x,y,BLUE)
            board[x][y] = a
            cost+= ARCHER_COST
        if(cost == TEAM_BLUE):
            break

    #set Team Red
    cost = 0
    print("Team Red")
    while(True):
        x, y = map(int,input("Enter the position of character").strip().split())
        print(y)
        if(y>=4 and board[x][y]==0 and cost+ARCHER_COST<=TEAM_BLUE):
            print("In if")
            a = Archer(x,y,RED)
            board[x][y] = a
            cost+= ARCHER_COST
        if(cost == TEAM_BLUE):
            break

def main():
    board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    # totalcostBlue = 100
    # totalcostRed = 100

    set_board(board)
    endTime = time.time() + 60

    #ToDO -> Player positions setting
    moves = 0
    if(is_correct_board(board)):
        while(time.time() < endTime):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(moves)
            for i in range(8):
                for j in range(8):
                    if(board[i][j]!=0):
                        board[i][j].move(board)
            print_board(board)
            moves+=1
            time.sleep(1)
            break
    else:
        print("Wrong Configuration")
    
    
if __name__ == "__main__":
    main()