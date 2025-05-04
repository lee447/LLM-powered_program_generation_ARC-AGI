def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h):
        row = grid[i]
        if 6 in row:
            # find all maximal runs of 6
            runs = []
            j = 0
            while j < w:
                if row[j] == 6:
                    k = j
                    while k < w and row[k] == 6:
                        k += 1
                    runs.append((j, k))
                    j = k
                else:
                    j += 1
            for start, end in runs:
                L = end - start
                # take the most frequent color in row excluding 6
                from collections import Counter
                cnt = Counter([c for c in row if c != 6])
                fill = cnt.most_common(1)[0][0]
                for x in range(start, end):
                    out[i][x] = fill
    return out