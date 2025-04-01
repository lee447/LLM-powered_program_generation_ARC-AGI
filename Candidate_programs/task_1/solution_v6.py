from collections import Counter
import numpy as np

def solve(grid):
    arr = np.array(grid, dtype=int)
    R, C = arr.shape
    # convert to int, make a copy for output
    res = arr.copy()
    # We'll apply an iterative “smoothing” that removes isolated pixels and forces consistency vertically.
    # In each iteration, for every non‐border cell:
    #  – If a nonzero cell has fewer than two horizontal nonzero neighbours, clear it.
    #  – If a nonzero cell’s left and right neighbours are equal and nonzero, set the cell to that value.
    #  – If a nonzero cell’s top and bottom neighbours are equal and nonzero, set the cell to that value.
    # We also clear the border each iteration.
    changed = True
    while changed:
        changed = False
        prev = res.copy()
        # clear borders
        res[0,:] = 0
        res[-1,:] = 0
        res[:,0] = 0
        res[:,-1] = 0
        new = res.copy()
        for i in range(1, R-1):
            for j in range(1, C-1):
                if res[i,j] != 0:
                    hor = [res[i, j-1], res[i, j+1]]
                    cnt = sum(1 for x in hor if x!=0)
                    if cnt < 2:
                        new[i,j] = 0
                    else:
                        if res[i, j-1] == res[i, j+1] and res[i, j-1] != 0:
                            new[i,j] = res[i, j-1]
                        ver = [res[i-1, j], res[i+1, j]]
                        if res[i-1, j] == res[i+1, j] and res[i-1, j] != 0:
                            new[i,j] = res[i-1, j]
        res = new.copy()
        if not np.array_equal(res, prev):
            changed = True

    # In a second pass, for each contiguous horizontal block of nonzero in each row,
    # if the block appears in adjacent rows too, then restrict the block to the common intersection.
    out = res.copy()
    for i in range(1, R-1):
        # find contiguous segments in row i
        segs = []
        j=0
        while j<C:
            if res[i,j]!=0:
                start = j
                while j<C and res[i,j]!=0:
                    j+=1
                end = j-1
                segs.append((start,end))
            else:
                j+=1
        if segs:
            # look at the previous and next rows (if nonzero segments exist there)
            for (s,e) in segs:
                interS, interE = s, e
                for ni in [i-1, i+1]:
                    # get segments in row ni that overlap with (s,e)
                    nsegs = []
                    k = 0
                    while k<C:
                        if res[ni,k]!=0:
                            ns = k
                            while k<C and res[ni,k]!=0:
                                k+=1
                            ne = k-1
                            nsegs.append((ns,ne))
                        else:
                            k+=1
                    for (ns,ne) in nsegs:
                        # if there is overlap, narrow the intersection
                        if ne>=s and ns<=e:
                            interS = max(interS, ns)
                            interE = min(interE, ne)
                # Outside the intersection, clear the row i.
                for j in range(s, e+1):
                    if j < interS or j > interE:
                        out[i,j] = 0
    return out.tolist()