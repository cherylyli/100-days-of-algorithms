from queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


def state_heuristic(puzzle, solved):
    """
    Given a puzzle, return how many moves is in solved state
    """
    sum = 0
    
    for i, row in enumerate(puzzle):
        for j, num in enumerate(row):
            if puzzle[i][j] != solved[num]:
                solved_i, solved_j = solved[num]
                sum += abs(solved_i - i) + abs(solved_j - j)

    return sum

def get_moves(puzzle):
    """
    Given a puzzle, get possible moves
    """
    # find 0
    pos_0 = None
    
    for i, row in enumerate(puzzle):
        if pos_0:
            break
        for j, num in enumerate(row):
            if num == 0:
                pos_0 = [i, j]
                break
    
    moves = ["UP", "RIGHT", "LEFT", "DOWN"]
    if pos_0[0] == 0:
        moves.remove("UP")
    if pos_0[0] == len(puzzle)-1:
        moves.remove("DOWN")
    if pos_0[1] == 0:
        moves.remove("LEFT")
    if pos_0[1] == len(puzzle) -1:
        moves.remove("RIGHT")
    return moves, pos_0

def swap(puzzle, pos_0, new_pos):
    """
        swap pos_0 and pos_to_move
    """
    temp = puzzle[pos_0[0]][pos_0[1]]
    puzzle[pos_0[0]][pos_0[1]] = puzzle[new_pos[0]][new_pos[1]]
    puzzle[new_pos[0]][new_pos[1]] = temp
    return puzzle
        
    
def toStr(puzzle):
    str_p = ""
    for row in puzzle:
        for num in row:
            str_p += str(num)
    return str_p
    
    
# get puzzle starting loc
n = int(input().strip())
puzzle_start = []
for i in range(n):
    new_line = []
    for j in range(n):
        new_line.append(int(input().strip()))
    puzzle_start.append(new_line)
   

solved_puzzle = {}
count = 0
for i in range(n):
    for j in range(n):
        solved_puzzle[count] = [i, j]
        count += 1
    
    
#print(solved_puzzle)

# initiate priority queue and put start state in
queue = MyPriorityQueue()
queue.put([[], puzzle_start, 0], 0+state_heuristic(puzzle_start, solved_puzzle))
solved = False
traversed = []
traversed.append(toStr(puzzle_start))

while not queue.empty() and not solved:
    curr_elem = queue.get()
    curr_moves = curr_elem[0]
    curr_puzzle = curr_elem[1]
    curr_num_moves = curr_elem[2]
    
    
    new_moves, pos_0 = get_moves(curr_puzzle)
    

    
    #print("current_elem, new moves")
    #print(curr_elem)
    #print(new_moves)
    
    for move in new_moves:
        if move == "UP":
            new_pos = [pos_0[0]-1, pos_0[1]]
        elif move == "DOWN":
            new_pos = [pos_0[0]+1, pos_0[1]]
        elif move == "LEFT":
            new_pos = [pos_0[0], pos_0[1]-1]
        else:
            new_pos = [pos_0[0], pos_0[1]+1]
        new_puzzle = [row[:] for row in curr_puzzle]
        new_puzzle = swap(new_puzzle, pos_0, new_pos)
        score = state_heuristic(new_puzzle, solved_puzzle)
        new_chain_moves = curr_moves[:]
        new_chain_moves.append(move)
        
        #print('new puzzle and score')
        #print(new_puzzle)
        #print(score)
        #print(curr_num_moves + 1 + score)
        
        if score == 0:
            
            print(len(new_chain_moves))
            for m in new_chain_moves:
                print(m)
            solved = True
        elif toStr(new_puzzle) not in traversed:
            queue.put([new_chain_moves, new_puzzle, curr_num_moves + 1], curr_num_moves + 1 + score)
            traversed.append(toStr(new_puzzle))
      
            
        



    
