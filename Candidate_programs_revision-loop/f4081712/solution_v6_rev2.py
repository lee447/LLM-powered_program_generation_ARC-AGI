from collections import Counter
def solve(grid):
    R, C = len(grid), len(grid[0])
    best = None
    for h in range(2, R+1):
        if R % h: continue
        for w in range(2, C+1):
            if C % w: continue
            total = (R//h)*(C//w)
            counts = Counter()
            for br in range(R//h):
                r0 = br*h
                for bc in range(C//w):
                    c0 = bc*w
                    block = tuple(tuple(grid[r0+i][c0+j] for j in range(w)) for i in range(h))
                    counts[block] += 1
            block, freq = counts.most_common(1)[0]
            if freq > total/2 and len({x for row in block for x in row}) > 1:
                if best is None or freq > best[0]:
                    best = (freq, block)
    return [list(row) for row in best[1]]