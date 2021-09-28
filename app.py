import time
import os


from test_cases import cases as case
from const import BLUE, RED, TEAM_BLUE, TEAM_RED, ARCHER_COST, TROOP_COST, CANNON_COST, ARCHER_HEALTH


class Characteristics:
    def __init__(self, x, y, color):
        # print(features)
        self.x = x
        self.y = y
        self.color = color

    
    def move(self,board):
        if(self.color == BLUE):
            distance = self.movementSpeed * 1
        else:
            distance = self.movementSpeed * -1
        if((self.y+distance<8 and self.y+distance>=0) and (board[self.x][self.y+distance]==0 or board[self.x][self.y+distance].cost==0)):
            board[self.x][self.y] = 0
            board[self.x][self.y+distance] = self
            self.y = self.y+distance


# class Troop(Characteristics):
#     def __init__(*p):
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
    def __init__(self, x, y, color):
        super().__init__(x,y, color)
        self.damage = 1
        self.attackSpeed = 0
        self.movementSpeed = 0
        self.cost = ARCHER_COST
        self.health = ARCHER_HEALTH
        self.isMovable = True
        self.isDestroyed = False
        

    
    #attack
    def attack(self,board):
        #ToDo-> add the concept of ismoving to void attacking when player moves
        if(self.y+1<8 and self.color==BLUE and board[self.x][self.y+1]!=0):
            if(board[self.x][self.y+1].color == RED):
                if(board[self.x][self.y+1].cost<=0):
                    board[self.x][self.y+1].cost=0
                else:
                    board[self.x][self.y+1].cost-=1
        if(self.y-1>=0 and self.color==RED and board[self.x][self.y-1]!=0):
            if(board[self.x][self.y-1].color == BLUE):
                if(board[self.x][self.y-1].cost<=0):
                    board[self.x][self.y-1].cost=0
                else:
                    board[self.x][self.y-1].cost-=1
        

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
                        board[i][j].attack(board)
                        if(board[i][j].isMovable == True):
                            board[i][j].move(board)
            print_board(board)
            moves+=1
            time.sleep(1)
            
    else:
        print("Wrong Configuration")
    
    
if __name__ == "__main__":
    main()