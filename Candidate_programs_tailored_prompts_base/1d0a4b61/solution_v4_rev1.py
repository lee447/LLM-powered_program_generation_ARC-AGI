from collections import Counter

def solve(grid):
    H, W = len(grid), len(grid[0])
    sep = [i for i,row in enumerate(grid) if all(v==1 for v in row)]
    res = [row[:] for row in grid]
    for k in range(len(sep)-1):
        B = sep[1]-sep[0]
        break
    blocks = len(sep)-1
    for off in range(1, B):
        rows = [tuple(grid[sep[b]+off]) for b in range(blocks)]
        exemplar = Counter(rows).most_common(1)[0][0]
        for b in range(blocks):
            res[sep[b]+off] = list(exemplar)
    return res