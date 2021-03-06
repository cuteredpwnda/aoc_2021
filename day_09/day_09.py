import numpy as np

def read_input(file = 'input/raw_input.txt'):
    return np.pad(np.genfromtxt(file, delimiter = 1), pad_width=1, mode='maximum')

def part1(b):
    # start at (1,1)
    is_min_list = []
    position_list = []
    for row in range(1,len(b)-1):
        for col in range(1,len(b[0])-1):
            center = b[row][col]
            up = b[row-1][col]
            down = b[row+1][col] 
            right = b[row][col+1]
            left = b[row][col-1]
            area = [up, down, right, left]
            if (center < min(area)):
                is_min_list.append(int(center))
                position_list.append((row, col))

    risk_level = np.add(is_min_list, 1).tolist()
    return sum(risk_level), position_list

def test():
    out = np.pad(np.array([[2,1,9,9,9,4,3,2,1,0],
                            [3,9,8,7,8,9,4,9,2,1],
                            [9,8,5,6,7,8,9,8,9,2],
                            [8,7,6,7,8,9,6,7,8,9],
                            [9,8,9,9,9,6,5,6,7,8]]),
                pad_width=1, mode='maximum')

    print('Result for part 1: ',part1(out))
    print('Result for part 2: ',part2(out))

def part2(b):
    return np.prod(sorted([len(x) for x in [bfs(x[0], x[1], b) for x in part1(b)[1]]])[-3:])    
    

def bfs(x:int,y:int, input_matrix:np.ndarray):
    start = [(x, y)]
    queue = start
    visited = set()
    while(queue):
        (curr_x, curr_y) = start.pop(0)
        if ((curr_x, curr_y) in visited or input_matrix[curr_x][curr_y] >= 9):
            continue
        visited.add((curr_x, curr_y))
        # add elements in order up, down, left, right
        queue.append((curr_x, curr_y-1))
        queue.append((curr_x, curr_y+1))
        queue.append((curr_x-1, curr_y))
        queue.append((curr_x+1, curr_y))
    return visited

if __name__ == '__main__':
    input_matrix = read_input()
    #test()
    p1,_ = part1(input_matrix)
    print('Result for part 1: ', p1)
    print('Result for part 2: ',part2(input_matrix))