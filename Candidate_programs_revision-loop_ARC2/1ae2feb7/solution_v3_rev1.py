from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    c = next(j for j in range(w) if all(grid[i][j] == 2 for i in range(h)))
    out = [row[:] for row in grid]
    for r in range(h):
        left = grid[r][:c]
        blocks = []
        i = 0
        while i < c:
            if left[i] != 0:
                v = left[i]
                start = i
                while i < c and left[i] == v:
                    i += 1
                blocks.append((v, i - start))
            else:
                i += 1
        blocks.reverse()
        for j in range(c + 1, w):
            k = j - (c + 1)
            val = 0
            for v, b in blocks:
                if k % b == 0:
                    val = v
                    break
            out[r][j] = val
    return out