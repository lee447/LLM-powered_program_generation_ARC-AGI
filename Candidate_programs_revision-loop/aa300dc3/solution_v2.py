def solve(grid):
    m, n = len(grid), len(grid[0])
    zeros = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0}
    best_chain = []
    for dr, dc in ((1, 1), (1, -1)):
        for i, j in zeros:
            if (i - dr, j - dc) not in zeros and (i + dr, j + dc) in zeros:
                chain = [(i, j)]
                x, y = i, j
                while (x + dr, y + dc) in zeros:
                    x += dr
                    y += dc
                    chain.append((x, y))
                if len(chain) > len(best_chain):
                    best_chain = chain
    output = [row[:] for row in grid]
    for i, j in best_chain:
        output[i][j] = 8
    return output