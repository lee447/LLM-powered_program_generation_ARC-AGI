def solve(grid):
    H = len(grid)
    W = len(grid[0])
    rot = [row[::-1] for row in grid[::-1]]
    top = [r + r[::-1] for r in rot]
    return top + top[::-1]

if __name__ == '__main__':
    import sys, json
    data = json.load(sys.stdin)
    out = solve(data)
    json.dump(out, sys.stdout)