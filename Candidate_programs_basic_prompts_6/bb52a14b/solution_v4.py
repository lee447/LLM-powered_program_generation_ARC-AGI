from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    templates = []
    for i in range(H-2):
        for j in range(W-2):
            sub = [grid[i+di][j:j+3] for di in range(3)]
            cnt = sum(1 for r in sub for v in r if v != 0)
            if cnt == 9:
                templates.append((cnt, sub))
    if not templates:
        for i in range(H-2):
            for j in range(W-2):
                sub = [grid[i+di][j:j+3] for di in range(3)]
                cnt = sum(1 for r in sub for v in r if v != 0)
                if cnt >= 7:
                    templates.append((cnt, sub))
    if not templates:
        return grid
    templates.sort(reverse=True, key=lambda x: x[0])
    template = templates[0][1]
    out = [row[:] for row in grid]
    for i in range(H-2):
        for j in range(W-2):
            ok = False
            for di in range(3):
                for dj in range(3):
                    v = grid[i+di][j+dj]
                    tv = template[di][dj]
                    if v != 0 and v != tv:
                        ok = False
                        break
                else:
                    continue
                break
            else:
                # check at least one zero to fill
                fill = any(grid[i+di][j+dj] == 0 and template[di][dj] != 0 for di in range(3) for dj in range(3))
                if fill:
                    for di in range(3):
                        for dj in range(3):
                            if out[i+di][j+dj] == 0 and template[di][dj] != 0:
                                out[i+di][j+dj] = template[di][dj]
    return out