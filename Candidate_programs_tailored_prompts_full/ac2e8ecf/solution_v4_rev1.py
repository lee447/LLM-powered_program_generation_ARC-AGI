from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not seen[r][c]:
                v = grid[r][c]
                pts = []
                stack = [(r, c)]
                seen[r][c] = True
                while stack:
                    x, y = stack.pop()
                    pts.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == v:
                            seen[nx][ny] = True
                            stack.append((nx, ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                clusters.append({
                    'pts': pts,
                    'v': v,
                    'r0': r0,
                    'c0': c0,
                    'h': r1 - r0 + 1,
                    'w': c1 - c0 + 1,
                    'n': len(pts)
                })
    g1, g2, g3 = [], [], []
    for cl in clusters:
        if cl['h'] == 3 and cl['w'] == 3 and cl['n'] == 8:
            g1.append(cl)
        elif cl['h'] == 4 and cl['w'] == 4 and cl['n'] >= 12:
            g2.append(cl)
        else:
            g3.append(cl)
    g1.sort(key=lambda c: c['c0'])
    g2.sort(key=lambda c: c['c0'])
    g3.sort(key=lambda c: c['c0'])
    out = [[0]*W for _ in range(H)]
    h1 = max((c['h'] for c in g1), default=0)
    off1 = 0
    off2 = off1 + h1
    h2 = max((c['h'] for c in g2), default=0)
    off3 = H - max((c['h'] for c in g3), default=0)
    for off, group in ((off1, g1), (off2, g2), (off3, g3)):
        for cl in group:
            dr = off - cl['r0']
            for x, y in cl['pts']:
                out[x + dr][y] = cl['v']
    return out