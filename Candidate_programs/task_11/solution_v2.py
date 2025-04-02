def solve(grid):
    h = len(grid)
    if h == 0: 
        return grid
    w = len(grid[0])
    # process each interior row (exclude first and last row--the fixed border)
    for r in range(1, h-1):
        interior = grid[r][1:w-1]
        L = len(interior)
        # if no interior cells, skip
        if L == 0:
            continue
        found = False
        for T in range(1, L+1):
            cand = [None]*T
            valid = True
            for i, val in enumerate(interior):
                if val != 0:
                    pos = i % T
                    if cand[pos] is None:
                        cand[pos] = val
                    elif cand[pos] != val:
                        valid = False
                        break
            if not valid:
                continue
            for i in range(L):
                mirror = L-1-i
                pos1 = i % T
                pos2 = mirror % T
                if cand[pos1] is not None and cand[pos2] is not None:
                    if cand[pos1] != cand[pos2]:
                        valid = False
                        break
            if not valid:
                continue
            # fill in missing candidate slots if possible using symmetry
            for i in range(T):
                if cand[i] is None:
                    # try to find a symmetric slot j with candidate value defined
                    j = (-1 - i) % T
                    if cand[j] is not None:
                        cand[i] = cand[j]
                    else:
                        cand[i] = 1
            # now fill in the row's interior using the candidate pattern
            new_interior = []
            for i in range(L):
                new_interior.append(cand[i % T])
            # enforce horizontal symmetry: ensure cell j equals cell L-1-j
            for i in range(L//2):
                new_interior[L-1-i] = new_interior[i]
            grid[r][1:w-1] = new_interior
            found = True
            break
        if not found:
            # if no cycle found, enforce horizontal symmetry directly
            interior = grid[r][1:w-1]
            L = len(interior)
            for i in range(L//2):
                if interior[i] == 0 and interior[L-1-i] != 0:
                    interior[i] = interior[L-1-i]
                elif interior[L-1-i] == 0 and interior[i] != 0:
                    interior[L-1-i] = interior[i]
                elif interior[i] == 0 and interior[L-1-i] == 0:
                    interior[i] = 1
                    interior[L-1-i] = 1
            grid[r][1:w-1] = interior
    return grid

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        out = solve(grid)
        sys.stdout.write(json.dumps(out))
    else:
        pass