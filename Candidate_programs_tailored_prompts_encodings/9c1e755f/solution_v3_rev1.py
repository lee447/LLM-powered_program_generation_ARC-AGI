from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited5 = [[False]*W for _ in range(H)]
    anchors = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5 and not visited5[r][c]:
                stack = [(r, c)]
                comp = []
                visited5[r][c] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 5 and not visited5[nx][ny]:
                            visited5[nx][ny] = True
                            stack.append((nx, ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                anchors.append((comp, min(rs), max(rs), min(cs), max(cs)))
    for comp, rmin, rmax, cmin, cmax in anchors:
        visited_seed = [[False]*W for _ in range(H)]
        seed_cells = set()
        for r, c in comp:
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] not in (0,5) and not visited_seed[nr][nc]:
                    stack = [(nr, nc)]
                    visited_seed[nr][nc] = True
                    while stack:
                        x, y = stack.pop()
                        seed_cells.add((x, y))
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            xx, yy = x+dx, y+dy
                            if 0 <= xx < H and 0 <= yy < W and grid[xx][yy] not in (0,5) and not visited_seed[xx][yy]:
                                visited_seed[xx][yy] = True
                                stack.append((xx, yy))
        if not seed_cells:
            continue
        if cmin == cmax:
            rows = sorted({r for r, _ in seed_cells})
            c0, c1 = min(c for _, c in seed_cells), max(c for _, c in seed_cells)
            seqs = [[grid[r][c] for c in range(c0, c1+1)] for r in rows]
            n = len(seqs)
            for r in range(rmin, rmax+1):
                seq = seqs[(r - rmin) % n]
                for j, v in enumerate(seq):
                    out[r][c0 + j] = v
        else:
            cols = sorted({c for _, c in seed_cells})
            r0, r1 = min(r for r, _ in seed_cells), max(r for r, _ in seed_cells)
            seqs = [[grid[r][c] for r in range(r0, r1+1)] for c in cols]
            n = len(seqs)
            for c in range(cmin, cmax+1):
                seq = seqs[(c - cmin) % n]
                for i, v in enumerate(seq):
                    out[r0 + i][c] = v
    return out