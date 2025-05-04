from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    blocks = []
    for r in range(h - 3):
        for c in range(w - 3):
            v = grid[r][c]
            if v == 0: continue
            good = True
            for i in range(4):
                for j in range(4):
                    x = grid[r + i][c + j]
                    if i in (0, 3) or j in (0, 3):
                        if x != v:
                            good = False
                            break
                    else:
                        if x != 0:
                            good = False
                            break
                if not good:
                    break
            if good:
                blocks.append((r, c, v))
    blocks.sort(key=lambda b: b[0])
    n = len(blocks)
    if n == 4:
        chosen = blocks[:2]
        out = [[ ] for _ in range(4)]
        for _, c, _ in sorted(chosen, key=lambda b: b[1]):
            for i in range(4):
                out[i].extend(grid[chosen[0][0]+i][c:c+4] if chosen[0][1]==chosen[0][1] else grid[chosen[0][0]+i][c:c+4])
        return out
    if n == 6:
        vs = [b[2] for b in blocks]
        mn, mx = min(vs), max(vs)
        mid = [b for b in blocks if b[2] not in (mn, mx)]
        mid.sort(key=lambda b: b[2], reverse=True)
        out = [[] for _ in range(4)]
        for r, c, _ in mid:
            for i in range(4):
                out[i].extend(grid[r+i][c:c+4])
        return out
    if n == 2:
        a, b = blocks
        ra, ca, _ = a
        rb, cb, _ = b
        if ra == rb:
            out = [grid[ra+i][ca:ca+4] + grid[rb+i][cb:cb+4] for i in range(4)]
        else:
            out = [grid[ra+i][ca:ca+4] for i in range(4)] + [grid[rb+i][cb:cb+4] for i in range(4)]
        return out
    # fallback
    return grid