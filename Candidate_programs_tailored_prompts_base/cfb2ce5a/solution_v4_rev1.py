from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    nonzeros = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    br = min(r for r, c in nonzeros)
    bc = min(c for r, c in nonzeros)
    n = 0
    for c in range(bc, w):
        if grid[br][c] != 0:
            n += 1
        else:
            break
    m = 0
    for r in range(br, h):
        if grid[r][bc] != 0:
            m += 1
        else:
            break
    n = m
    out = [[0]*w for _ in range(h)]
    for r in range(1, h-1):
        for c in range(1, w-1):
            if br <= r < br+n and bc <= c < bc+n:
                out[r][c] = grid[r][c]
    def fill_block(r0, c0):
        dist = [[None]*n for _ in range(n)]
        owner = [[0]*n for _ in range(n)]
        Q = deque()
        for r in range(r0, r0+n):
            for c in range(c0, c0+n):
                v = grid[r][c]
                if v != 0 and not (br <= r < br+n and bc <= c < bc+n):
                    rr, cc = r-r0, c-c0
                    dist[rr][cc] = 0
                    owner[rr][cc] = v
                    Q.append((rr, cc, v))
        while Q:
            r, c, v = Q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                rr, cc = r+dr, c+dc
                if 0 <= rr < n and 0 <= cc < n:
                    nd = dist[r][c] + 1
                    if dist[rr][cc] is None or nd < dist[rr][cc] or (nd == dist[rr][cc] and v < owner[rr][cc]):
                        dist[rr][cc] = nd
                        owner[rr][cc] = v
                        Q.append((rr, cc, v))
        for rr in range(n):
            for cc in range(n):
                out[r0+rr][c0+cc] = owner[rr][cc]
    fill_block(br, bc+n)
    fill_block(br+n, bc)
    fill_block(br+n, bc+n)
    return out