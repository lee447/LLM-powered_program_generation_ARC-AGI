from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    shapes = []
    for i in range(R-2):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                cnt = 0
                while stack:
                    x, y = stack.pop()
                    cnt += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R-2 and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                shapes.append((cnt, col))
    holes = []
    j = 0
    row = grid[R-2]
    while j < C:
        if row[j] == 0:
            start = j
            length = 0
            while j < C and row[j] == 0:
                length += 1
                j += 1
            holes.append((start, length))
        else:
            j += 1
    out = [[0]*C for _ in range(R)]
    for j in range(C):
        out[R-2][j] = grid[R-2][j]
        out[R-1][j] = grid[R-1][j]
    for size, col in shapes:
        length = size // 2
        for seg in holes:
            start, l = seg
            if l == length:
                for i in (R-2-1, R-2):
                    for jj in range(start, start+length):
                        out[i][jj] = col
                holes.remove(seg)
                break
    return out