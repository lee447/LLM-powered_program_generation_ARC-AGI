from collections import Counter
def solve(grid):
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # compute non‐background counts per row
    rowcnt = [sum(1 for x in row if x) for row in grid]
    nonzero_counts = [s for s in rowcnt if s]
    thr = (sum(nonzero_counts)/len(nonzero_counts)) / 2 if nonzero_counts else 0
    for i in range(R):
        if rowcnt[i] < thr:
            out[i] = [0]*C
    # group contiguous rows that are not blank
    groups = []
    i = 0
    while i < R:
        if out[i] != [0]*C:
            start = i
            while i < R and out[i] != [0]*C:
                i += 1
            groups.append((start, i-1))
        else:
            i += 1
    # For each group, adjust the top row by “cleaning” each contiguous block
    for s,e in groups:
        row = out[s]
        newrow = row[:]
        j = 0
        while j < C:
            if row[j] == 0:
                j += 1
            else:
                startj = j
                while j < C and row[j] != 0:
                    j += 1
                block = row[startj:j]
                if block:
                    mode = Counter(block).most_common(1)[0][0]
                    for k in range(startj, j):
                        newrow[k] = mode
        out[s] = newrow
    return out