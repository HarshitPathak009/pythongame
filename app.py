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
            distance = self.movementDistance * 1
        else:
            distance = self.movementDistance * -1
        if((self.y+distance<8 and self.y+distance>=0) and (board[self.x][self.y+distance]==0 or board[self.x][self.y+distance].health==0)):
            board[self.x][self.y] = 0
            board[self.x][self.y+distance] = self
            self.y = self.y+distance


class Troop(Characteristics):
    def __init__(self, x, y, color):
        super().__init__(x,y, color)
        self.damage = 1
        self.attackDistance = 0
        self.movementDistance = 2
        self.cost = TROOP_COST
        self.health = TROOP_COST
        self.isMovable = True
    
    def attack(self,board):
        pass

        
    #move

    #health

    #destroy


class Cannon(Characteristics):
    def __init__(self, x,y,color):
        super().__init__(x,y, color)
        self.damage = 1
        self.attackDistance = 0
        self.movementDistance = 0
        self.cost = CANNON_COST
        self.health = CANNON_COST
        self.isMovable = False
    
    #attack
    def attack(self, board):
        pass
        
    #move

    #health

    #destroy


class Archer(Characteristics):
    def __init__(self, x, y, color):
        super().__init__(x,y, color)
        self.damage = 1
        self.attackDistance = 0
        self.movementDistance = 1
        self.cost = ARCHER_COST
        self.health = ARCHER_COST
        self.isMovable = True
        

    
    #attack
    def attack(self,board):
        #ToDo-> add the concept of ismoving to void attacking when player moves
        if(self.y+1<8 and self.color==BLUE and board[self.x][self.y+1]!=0):
            if(board[self.x][self.y+1].color == RED):
                if(board[self.x][self.y+1].health<=0):
                    board[self.x][self.y+1].health=0
                else:
                    board[self.x][self.y+1].health-=1
        if(self.y-1>=0 and self.color==RED and board[self.x][self.y-1]!=0):
            if(board[self.x][self.y-1].color == BLUE):
                if(board[self.x][self.y-1].health<=0):
                    board[self.x][self.y-1].health=0
                else:
                    board[self.x][self.y-1].health-=1
        

def print_board(board):
    for i in range(8):
        for j in range(8):
            if(board[i][j]!=0):
                print(board[i][j].health,end="\t")
                continue
            print(board[i][j],end="\t")
        print("")

def Winner(board):
    remainingBlueHealth = 0
    remainingRedHealth = 0

    #left-side cost
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]!=0):
                if(board[i][j].color == RED):
                    remainingRedHealth+=board[i][j].health
                else:
                    remainingBlueHealth+=board[i][j].health
    # print(cost)
    # print(remainingRedHealth)
    # print(remainingBlueHealth)
    if(remainingRedHealth>remainingBlueHealth):
        print("TEAM RED WINS")
    elif(remainingBlueHealth>remainingRedHealth):
        print("TEAM BLUE WINS")
    else:
        print("IT's a DRAW")


def set_board(board):
    #set Team Blue
    cost = 0
    print("Team Blue")
    while(True):
        name = int(input("Enter 1 for Troops, 2 for Archer, 3 for Cannon"))
        if(name>3 or name<=0):
            print("Please enter the given options")
            continue
        x, y = map(int,input("Enter the position of character").strip().split())
        if(name == 1):
            if(y<=3 and board[x][y]==0 and cost+TROOP_COST<=TEAM_BLUE):
                a = Troop(x,y,BLUE)
                board[x][y] = a
                cost+= TROOP_COST
        elif(name ==2):
            if(y<=3 and board[x][y]==0 and cost+ARCHER_COST<=TEAM_BLUE):
                a = Archer(x,y,BLUE)
                board[x][y] = a
                cost+= ARCHER_COST
        else:
            if(y<=3 and board[x][y]==0 and cost+CANNON_COST<=TEAM_BLUE):
                a = Cannon(x,y,BLUE)
                board[x][y] = a
                cost+= CANNON_COST
        print("Remaining Cost = ", TEAM_BLUE-cost)
        if(cost == TEAM_BLUE):
            break

    #set Team Red
    cost = 0
    print("Team Red")
    while(True):
        name = int(input("Enter 1 for Troops, 2 for Archer, 3 for Cannon"))
        if(name>3 or name<=0):
            print("Please enter the given options")
            continue
        x, y = map(int,input("Enter the position of character").strip().split())
        if(name == 1):
            if(y>3 and board[x][y]==0 and cost+TROOP_COST<=TEAM_RED):
                a = Troop(x,y,RED)
                board[x][y] = a
                cost+= TROOP_COST
        elif(name ==2):
            if(y>3 and board[x][y]==0 and cost+ARCHER_COST<=TEAM_RED):
                a = Archer(x,y,RED)
                board[x][y] = a
                cost+= ARCHER_COST
        else:
            if(y>3 and board[x][y]==0 and cost+CANNON_COST<=TEAM_RED):
                a = Cannon(x,y,RED)
                board[x][y] = a
                cost+= CANNON_COST
        print("Remaining Cost = ", TEAM_RED-cost)
        if(cost == TEAM_RED):
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
    # if(is_correct_board(board)):
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
    Winner(board)
    
    
if __name__ == "__main__":
    main()