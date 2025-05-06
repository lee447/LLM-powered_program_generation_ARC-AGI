def solve(grid):
    h = len(grid)
    w = len(grid[0])
    sepRows = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    sepCols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    blockRows = len(sepRows) - 1
    blockCols = len(sepCols) - 1
    blockHeight = sepRows[1] - sepRows[0] - 1
    blockWidth = sepCols[1] - sepCols[0] - 1
    pattern = []
    topStart = sepRows[0] + 1
    for bc in range(blockCols):
        leftStart = sepCols[bc] + 1
        block = [grid[r][leftStart:leftStart+blockWidth] for r in range(topStart, topStart+blockHeight)]
        pattern.append(block)
    out = [row[:] for row in grid]
    for br in range(1, blockRows):
        rowStart = sepRows[br] + 1
        for bc in range(blockCols):
            colStart = sepCols[bc] + 1
            pat = pattern[bc]
            for dr in range(blockHeight):
                out[rowStart+dr][colStart:colStart+blockWidth] = pat[dr][:]
    return out