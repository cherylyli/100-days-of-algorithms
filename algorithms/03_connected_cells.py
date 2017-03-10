# may be able to optimize better, need to think more


def get_untraversed_neighbors(cell, region, matrix, untraversed, traversed):
    """
        input: a cell, a region array, which contains all cells that are in this region, and the bounds m & n
        output: a Boolean that indicates whether the cell has more neighbors in that region, and also returns the region array
    """
    x,y = cell
    to_test = []
    pos_nodes = []
    neg_nodes = []
    deltas = [-1, 0, 1]
    for dx in deltas:
        for dy in deltas:
            new_node = (x+dx, y+dy)
            # if it's a new node we haven't encountered before, section it based on whether it's a 1 or 0 in matrix
            if new_node not in region and new_node in untraversed:
                if matrix[new_node[0]][new_node[1]] == 1:
                    pos_nodes.append(new_node)
                else: 
                    neg_nodes.append(new_node)
                untraversed.remove(new_node)
                traversed.append(new_node)

    return pos_nodes, neg_nodes

def get_region(traversed, frontier, region, matrix, untraversed):
    """
        input: a frontier, the traversed & untraversed nodes, the matrix, and then current nodes in the current region
        output: the full region
    """
    # base case, frontier is empty, return
    if len(frontier) == 0:
        return region

    current_node = frontier[0]
    frontier = frontier[1:]
    new_pos_nodes, new_neg_nodes = get_untraversed_neighbors(current_node, region, matrix, untraversed, traversed)

    if len(new_pos_nodes) > 0:
        frontier += new_pos_nodes
        region += new_pos_nodes
        return get_region(traversed, frontier, region, matrix, untraversed)
    
    # if no new_pos_nodes, return
    else:
        return get_region(traversed, frontier, region, matrix, untraversed)
    
    
    
def find_next_one(untraversed, traversed, matrix):
    """
    find next node in matrix that's a 1 and also untraversed yet
    """
    for node in untraversed:
        if matrix[node[0]][node[1]] == 1:
            untraversed.remove(node)
            traversed.append(node)
            return node
    return None

m = int(input().strip())
n = t = int(input().strip())

# construct m by n matrix
matrix = []

for m_index in range(m):
    new_line = [int(s) for s in input().split(" ")]
    matrix.append(new_line)
    
traversed_nodes = []
untraversed_nodes = [(m_ind, n_ind) for m_ind in range(m) for n_ind in range(n)]
max_region = 0

base_node = find_next_one(untraversed_nodes, traversed_nodes, matrix)

while base_node:
    new_region = get_region(traversed_nodes, [base_node], [base_node], matrix, untraversed_nodes)
    max_region = len(new_region) if len(new_region) > max_region else max_region
    base_node = find_next_one(untraversed_nodes, traversed_nodes, matrix)
    

print(max_region)
