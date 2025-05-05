def solve(grid):
    H, W = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 1 and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                region = []
                touches = False
                seed_color = None
                seed_count = 0
                while stack:
                    rr, cc = stack.pop()
                    region.append((rr, cc))
                    if rr==0 or rr==H-1 or cc==0 or cc==W-1:
                        touches = True
                    v = grid[rr][cc]
                    if v not in (0,1):
                        seed_count += 1
                        seed_color = v
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W:
                            if not visited[nr][nc] and grid[nr][nc] != 1:
                                visited[nr][nc] = True
                                stack.append((nr,nc))
                if not touches and seed_count == 1:
                    for rr, cc in region:
                        if res[rr][cc] != 1:
                            res[rr][cc] = seed_color
    return res