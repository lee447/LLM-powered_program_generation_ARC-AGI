from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not visited[i][j]:
                comp = []
                dq = deque()
                dq.append((i,j))
                visited[i][j] = True
                while dq:
                    r,c = dq.popleft()
                    comp.append((r,c))
                    for dr,dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w:
                            if grid[nr][nc] and not visited[nr][nc] and grid[nr][nc]==grid[r][c] or (grid[nr][nc] and not visited[nr][nc] and grid[nr][nc]!=0):
                                if not visited[nr][nc]:
                                    if grid[nr][nc] != 0:
                                        visited[nr][nc] = True
                                        dq.append((nr,nc))
                min_r = min(r for r,_ in comp)
                max_r = max(r for r,_ in comp)
                min_c = min(c for _,c in comp)
                max_c = max(c for _,c in comp)
                touches_border = (min_r==0 or max_r==h-1 or min_c==0 or max_c==w-1)
                if not touches_border:
                    counts = {}
                    for r,c in comp:
                        counts[grid[r][c]] = counts.get(grid[r][c],0)+1
                    mode = max(counts, key=lambda x: counts[x])
                    for r in range(min_r, max_r+1):
                        for c in range(min_c, max_c+1):
                            out[r][c] = mode
    return out

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read()
    if data:
        grid = json.loads(data)
        result = solve(grid)
        print(json.dumps(result))
else:
    None