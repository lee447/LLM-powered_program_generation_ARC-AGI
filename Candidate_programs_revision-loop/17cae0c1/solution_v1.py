from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    bw = W // 3
    mapping = {'ring': 3, 'dot': 4, 'top': 6, 'bottom': 1, 'anti': 9}
    colors = []
    for bi in range(3):
        block = [row[bi * bw:(bi + 1) * bw] for row in grid]
        coords = [(r, c) for r in range(H) for c in range(bw) if block[r][c] == 5]
        cnt = len(coords)
        if cnt == 1:
            t = 'dot'
        elif all(block[0][c] == 5 for c in range(bw)) and all(block[r][c] == 0 for r in range(1, H) for c in range(bw)):
            t = 'top'
        elif all(block[H-1][c] == 5 for c in range(bw)) and all(block[r][c] == 0 for r in range(H-1) for c in range(bw)):
            t = 'bottom'
        elif all((r + c == bw - 1 and block[r][c] == 5) or (r + c != bw - 1 and block[r][c] == 0) for r in range(H) for c in range(bw)):
            t = 'anti'
        else:
            t = 'ring'
        colors.extend([mapping[t]] * bw)
    return [colors[:] for _ in range(H)]