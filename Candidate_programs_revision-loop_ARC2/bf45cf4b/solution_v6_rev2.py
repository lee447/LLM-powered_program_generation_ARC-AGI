from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = Counter(flat).most_common(1)[0][0]
    def is_sym(b):
        k = len(b)
        for i in range(k):
            for j in range(k):
                if b[i][j] != b[k-1-j][i]:
                    return False
        return True
    best = None
    best_k = 0
    for k in range(min(h, w), 1, -1):
        found = []
        for i in range(h-k+1):
            for j in range(w-k+1):
                b = [row[j:j+k] for row in grid[i:i+k]]
                if is_sym(b):
                    cols = {x for row in b for x in row if x != bg}
                    found.append((i, j, b, len(cols)))
        if found:
            i, j, b, _ = max(found, key=lambda x: (x[3], -x[0], -x[1]))
            best = b
            best_k = k
            break
    k = best_k
    b = best
    nb_row = h // k
    nb_col = w // k
    keep_r = set()
    keep_c = set()
    for bi in range(nb_row):
        for bj in range(nb_col):
            for x in range(k):
                for y in range(k):
                    if grid[bi*k+x][bj*k+y] != bg:
                        keep_r.add(bi)
                        keep_c.add(bj)
    sr = max(min(keep_r) - 1, 0)
    er = min(max(keep_r) + 1, nb_row - 1)
    sc = max(min(keep_c) - 1, 0)
    ec = min(max(keep_c) + 1, nb_col - 1)
    H = (er - sr + 1) * k
    W = (ec - sc + 1) * k
    out = [[bg] * W for _ in range(H)]
    for bi in range(sr, er + 1):
        for bj in range(sc, ec + 1):
            for x in range(k):
                for y in range(k):
                    out[(bi - sr) * k + x][(bj - sc) * k + y] = b[x][y]
    return out