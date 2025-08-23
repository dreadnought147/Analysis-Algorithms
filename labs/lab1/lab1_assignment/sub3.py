import sys
from collections import deque

# Global space to store the 3x3 board
space = []

def print_Arr(arr):
    strr = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            strr += arr[i][j]
    print(strr)
    return

def check_move(x, y, direction):
    if direction == "LEFT":
        if not (x < 0 or y-1 < 0 or x > 2 or y > 2):
            return (x, y-1)
        return "invalid move"
    if direction == "RIGHT":
        if not (x < 0 or y < 0 or x > 2 or y+1 > 2):
            return (x, y+1)
        return "invalid move"
    if direction == "UP":
        if not (x-1 < 0 or y < 0 or x > 2 or y > 2):
            return (x-1, y)
        return "invalid move"
    if direction == "DOWN":
        if not (x < 0 or y < 0 or x+1 > 2 or y > 2):
            return (x+1, y)
        return "invalid move"

def hash_place(space):
    # Find position of '#' (blank tile) in the board
    item = "#"
    for i in range(len(space)):
        if item in space[i]:
            return (i, space[i].index(item))

def move_take(inputt):
    # Validate input length and convert string to 2D board
    if len(inputt) != 9:
        return "Input is too long or too short"
    global space
    space.clear()
    count = 0
    for i in range(3):
        inner = []
        for j in range(3):
            inner.append(inputt[count])
            count += 1
        space.append(inner)
    return

def make_move(blank, move):
    # Perform move by swapping blank tile with target position
    if isinstance(move, str):
        return "not a valid move"
    x1, y1 = blank
    x2, y2 = move
    temp = space[x1][y1]
    space[x1][y1] = space[x2][y2]
    space[x2][y2] = temp
    return

def board_to_string(board):
    string = ""
    for i in board: 
        string = string + ''.join(i)
    return string
def board_str_to_space(board_str):
    # Convert string to 2D board and update global space
    global space  #tells we are using the global defn 
    space.clear()# clear its contents
    #space declariton is a strign
    count = 0 
    for i in range(3):
        row = []
        for j in range(3):
            row.append(board_str[count])
            count += 1
        space.append(row)



def run(state_str, direction):
    # Attempt a move on given state and return new state string or None if invalid
    global space
    board_str_to_space(state_str) #convertt the boards string into the space 
    blank = hash_place(space) #find the hash
    move_pos = check_move(blank[0], blank[1], direction) #check if we can move hash in the stipulated direction

    if isinstance(move_pos, str) and "invalid" in move_pos:
        return None

    make_move(blank, move_pos) #otehrwise continue and actually make the move in the stipulated direction
    new_state = board_to_string(space) #the borad is upadtes so lets see what it looks like as a string?
    return new_state 

def bfs_shortest_path(initial_state, goal_state):
    # Perform BFS to find shortest path cost from initial to goal state
    visited = set() #part of our huertsic will decrease our time andd space complexity
    queue = deque([(initial_state, 0)])  # (state, cost)
    visited.add(initial_state)
    moves = ["LEFT", "UP", "DOWN", "RIGHT"]

    while queue:
        current_state, cost = queue.popleft() #pop the first item in the queue everything in queue is stored as a state 
                                                #and a int value
                                                #Last cost it pops will be the cost of reaching the goal node
        
        # Check if goal state is reached
        if current_state == goal_state:
            return cost

        # Try all possible moves
        for move in moves:
            new_state = run(current_state, move) #create a new state based on what will result if we run in that dire so that siccesor
            if new_state and new_state not in visited: #if its not none and is not in visted then 
                visited.add(new_state)
                queue.append((new_state, cost + 1)) #state is 1 increasing 

    return -1  # No path found


initial_state = input().strip()
goal_state = input().strip()

# Validate input
if len(initial_state) != 9 or len(goal_state) != 9:
    print("Invlaid ipmut length")
    sys.exit()

# Run BFS and output result
result = bfs_shortest_path(initial_state, goal_state)
print(result)
