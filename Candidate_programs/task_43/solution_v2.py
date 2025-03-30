from typing import List
import sys
sys.setrecursionlimit(10000)
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    if n==0: 
        return grid
    m = len(grid[0])
    visited = [[False]*m for _ in range(n)]
    comps = []
    def dfs(i,j,comp):
        stack = [(i,j)]
        visited[i][j] = True
        while stack:
            ci, cj = stack.pop()
            comp.append((ci,cj))
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and grid[ni][nj]==2:
                    visited[ni][nj] = True
                    stack.append((ni,nj))
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2 and not visited[i][j]:
                comp = []
                dfs(i,j,comp)
                comps.append(comp)
    # Heuristic rule:
    # For each connected group of 2's, compute average row and col.
    # Then recolor the entire component to 8 if either:
    #  - its average row is in the top half of the grid and its average col is not very left, or
    #  - its average row is in the bottom half and its average col is very far to the right.
    for comp in comps:
        avg_row = sum(i for i,j in comp)/len(comp)
        avg_col = sum(j for i,j in comp)/len(comp)
        flip = False
        if avg_row < n/2:
            if avg_col > m/4:
                flip = True
        else:
            if avg_col > 3*m/4:
                flip = True
        if flip:
            for i,j in comp:
                grid[i][j] = 8
    return grid

if __name__=="__main__":
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        ans = solve(grid)
        sys.stdout.write(json.dumps(ans))
    else:
        sys.stdout.write("[]")