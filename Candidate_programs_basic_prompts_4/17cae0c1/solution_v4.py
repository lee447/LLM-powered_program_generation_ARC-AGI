from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    blocks = w // 3
    out_row = []
    for b in range(blocks):
        pos = {(i, j) for i in range(3) for j in range(3) if grid[i][b*3+j] == 5}
        if len(pos) == 1:
            c = 4
        elif len(pos) == 8:
            c = 3
        else:
            if pos == {(0,2),(1,1),(2,0)}:
                c = 9
            elif all((0,j) in pos for j in range(3)):
                c = 6
            else:
                c = 1
        out_row += [c, c, c]
    return [list(out_row) for _ in range(h)]