from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    block, gap = 2, 1
    anchorRow = next(i for i, row in enumerate(grid) if any(v not in (0,1,5) for v in row))
    # detect grey-band starting rows
    greyStarts = []
    for i in range(h-1):
        if any(grid[i][j]==5 for j in range(w)) and any(grid[i+1][j]==5 for j in range(w)):
            if i==0 or not any(grid[i-1][j]==5 for j in range(w)):
                greyStarts.append(i)
    # detect grey-band columns from first grey start
    r0 = greyStarts[0]
    greyCols = [j for j in range(w-block+1)
                if all(grid[r0+di][j+dj]==5 for di in (0,1) for dj in (0,1))]
    greyCols.sort()
    # detect anchor columns if top-row anchor
    hasAnchor = (anchorRow == 0)
    if hasAnchor:
        anchorCols = []
        for j in range(w-block+1):
            c = grid[anchorRow][j]
            if c in (0,1,5): continue
            if all(grid[anchorRow+di][j+dj]==c for di in (0,1) for dj in (0,1)):
                anchorCols.append(j)
        anchorCols.sort()
    # decide insert bands
    insertStarts = greyStarts if not hasAnchor else greyStarts[1:]
    bands = (1 if hasAnchor else 0) + len(insertStarts)
    height = bands*block + (bands-1)*gap
    width = len(greyCols)*block + (len(greyCols)-1)*gap
    out = [[0]*width for _ in range(height)]
    # fill anchor band
    if hasAnchor:
        for idx, j in enumerate(anchorCols):
            c = grid[anchorRow][j]
            out_r = 0
            off = idx*(block+gap)
            for di in range(block):
                for dj in range(block):
                    out[out_r+di][off+dj] = c
    # fill insert bands
    for k, rstart in enumerate(insertStarts):
        bandIdx = k + (1 if hasAnchor else 0)
        out_r = bandIdx*(block+gap)
        for idx, j in enumerate(greyCols):
            val = 0
            for di in range(block):
                for dj in range(block):
                    v = grid[rstart+di][j+dj]
                    if v not in (0,5):
                        val = v
            if val:
                off = idx*(block+gap)
                for di in range(block):
                    for dj in range(block):
                        out[out_r+di][off+dj] = val
    return out