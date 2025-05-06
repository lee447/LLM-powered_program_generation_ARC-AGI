from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    row1, row2 = grid
    x = row2.index(0) + 1
    y = 0
    path = [(x, y)]
    h_dir = 1
    h_steps = 0
    for i in range(len(row1)):
        if row2[i] == 2:
            y += 1
            path.append((x, y))
        if row1[i] == 2:
            x += h_dir
            path.append((x, y))
            h_steps += 1
            h_dir *= -1
    H = sum(1 for v in row2 if v == 2)
    W = h_steps + 2
    out = [[0] * W for _ in range(H)]
    for idx, (cx, cy) in enumerate(path):
        if 0 <= cy < H and 0 <= cx < W:
            out[cy][cx] = 3 if idx == 0 else 2
    return out