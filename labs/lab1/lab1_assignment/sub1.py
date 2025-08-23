import sys
def print_Arr(arr):
    strr=""
    for i in range(len(arr)):
        for j in range(0,len(arr[i])):
            strr=strr+arr[i][j]
    print(strr)
    return
            
def check_move(x,y):
    if direction=="LEFT":
        if not ( y-1<0 or x>2 or y>2):
            return (x,y-1)
        else:
            return "invalid move"
    if direction=='RIGHT':
        if not (x<0 or y<0 or x>2 or y+1>2):
            return (x,y+1)
        else:
            return "invalid move"
    if direction=='UP':
        if not (x-1<0 or y<0 or x>2 or y>2):
            return (x-1,y)
        else:
            print("we entered up") 
            return "invalid move"
    if direction=='DOWN':
        if not (x<0 or y<0 or x+1>2 or y>2):
            return (x+1,y)
        else:
            return "invalid move"

def hash_place(space):
    item ="#"
    for i in range(0, len(space)):
        if item in space[i]:
            return (i,space[i].index(item))
def move_take(inputt):
    cont = False
    if (len(inputt)==9):
        cont=True
    else:
        return "Input is too long or too short"
    count =0
    for i in range(0,3):
        inner = []
        for j in range (0,3):
            inner.append(inputt[count])
            count = count+1
        space.append(inner)
    return
def make_move(blank, move):
    if isinstance(move, str):
        #print("MOVE IS THIS : ",move)
        return None
    x1 = blank[0]
    y1 = blank[1]
    #print(blank, ": where the hash is ")
    x2 = move[0]
    y2 = move[1]
    #print(move, ": the next move")
    temp = space[x1][y1]
    space[x1][y1] = space[x2][y2]
    space[x2][y2] = temp
    print_Arr(space)
    return 

space =[]
inputt = str(input())
direction = str(input())
moves= ["UP", "DOWN", "LEFT", "RIGHT"]
def run():
    move_take(inputt)
    if len(space)==0:
        print("invalid 8puzzle configuration")
        print(space)
        return
    if (direction) not in moves:
        print("inavlid direction")
        print(space)
        return
    blank = hash_place(space)
    #print("blank is avail", blank)
    move = check_move(blank[0],blank[1])
    make_move(blank, move)

run()
