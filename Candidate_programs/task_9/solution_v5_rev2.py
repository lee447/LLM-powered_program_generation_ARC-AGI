from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    frames = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 5 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                pts = []
                while stack:
                    r,c = stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<H and 0<=cc<W and not visited[rr][cc] and grid[rr][cc]==5:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                rs = [r for r,c in pts]; cs = [c for r,c in pts]
                top, bot, left, right = min(rs), max(rs), min(cs), max(cs)
                frames.append((top, bot, left, right))
    out = [row[:] for row in grid]
    for top,bot,left,right in frames:
        for c in range(left, right+1):
            if out[top][c] == 0: out[top][c] = 2
            if out[bot][c] == 0: out[bot][c] = 2
        for r in range(top, bot+1):
            if out[r][left] == 0: out[r][left] = 2
            if out[r][right] == 0: out[r][right] = 2
        for r in range(top+1, bot):
            for c in range(left+1, right):
                if out[r][c] == 0: out[r][c] = 2
    for top,bot,left,right in frames:
        sr = top-1
        if sr < 0: continue
        hole = None
        for c in range(left, right+1):
            if grid[top][c] == 0:
                hole = c
                break
        if hole is None: continue
        if hole-left < right-hole:
            start, end = hole, W-1
        else:
            start, end = 0, hole
        for c in range(start, end+1):
            if out[sr][c] == 0:
                out[sr][c] = 2
    return out