import itertools

def solution(relation):
    result = []
    rowlen = len(relation)
    collen = len(relation[0])

    collist = [n for n in range(collen)]

    colcombi = []

    for n in range(1, collen + 1):
        colcombi.extend(set(itertools.combinations(collist, n)))

    for col in colcombi:
        tmplist = []
        colcheck = True

        for resultset in result:
            s = set(resultset) < set(col)

            if s:
                colcheck = False
                break

        if colcheck:
            for row in range(rowlen):
                tmp = []
                for c in col:
                    tmp.append(relation[row][c])

                if tmp not in tmplist:
                    tmplist.append(tmp)

            if len(tmplist) == rowlen:
                result.append(col)

    return len(result)