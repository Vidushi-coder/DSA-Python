from collections import deque

def rotting_oranges(grid):
    queue = deque()
    fresh = 0
    minutes = 0

    r = len(grid)
    c = len(grid[0])
    
    for i in range(r):
       for j in range(c):
           if grid[i][j] == 2:
               queue.append((i,j))
           elif grid[i][j] == 1:
               fresh += 1

    if fresh == 0:
        return 0

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    while queue and fresh>0:
        level_size = len(queue)

        for _ in range(level_size):
            i,j = queue.popleft()

            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]

                if(0<=nr<r and 0<=nc<c and grid[nr][nc]==1):
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh -= 1

        minutes += 1

    if fresh == 0:
        return minutes

    return -1

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(rotting_oranges(grid))  