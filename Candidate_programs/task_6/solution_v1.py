def solve(grid):
    rows = len(grid)
    if rows == 0:
        return grid
    cols = len(grid[0])
    def is_divider(r):
        return all(x==0 for x in r)
    pat_index = None
    for i,r in enumerate(grid):
        if not is_divider(r):
            pat_index = i
            break
    if pat_index is None:
        return grid
    ref = grid[pat_index]
    blocks = []
    i = 0
    while i < cols:
        j = i+1
        while j < cols and ref[j] == ref[i]:
            j += 1
        blocks.append((i, j, ref[i]))
        i = j
    trans = []
    for idx,(s,e,v) in enumerate(blocks):
        if idx != 0 and idx != len(blocks)-1 and v == 0:
            trans.append(2)
        else:
            trans.append(v)
    non_bottom = []
    for idx, val in enumerate(trans):
        if idx==0 or idx==len(trans)-1:
            non_bottom.append(1 if val==0 else 2)
        else:
            non_bottom.append(2)
    bottom_fill = []
    for idx,_ in enumerate(trans):
        if idx==0 or idx==len(trans)-1:
            bottom_fill.append(0)
        else:
            bottom_fill.append(1)
    pat_rows = [i for i,r in enumerate(grid) if not is_divider(r)]
    max_pat = max(pat_rows) if pat_rows else -1
    out = []
    for r_idx, row in enumerate(grid):
        if not is_divider(row):
            newrow = [None]*cols
            for b, (s,e,v) in enumerate(blocks):
                for i in range(s, e):
                    if b != 0 and b != len(blocks)-1 and v==0:
                        newrow[i] = 2
                    else:
                        newrow[i] = row[i]
            out.append(newrow)
        else:
            newrow = [None]*cols
            fill = non_bottom if r_idx < max_pat else bottom_fill
            for b, (s,e,_) in enumerate(blocks):
                for i in range(s, e):
                    newrow[i] = fill[b]
            out.append(newrow)
    return out

if __name__ == '__main__':
    import json,sys
    data = sys.stdin.read().strip()
    if data:
        inp = json.loads(data)
        out = solve(inp)
        sys.stdout.write(json.dumps(out))
    else:
        pass