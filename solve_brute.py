import full_verify
import full_create
import time



def solve(list):
    start = time.time()
    now = start
    verify = False

    sq_id = full_create.gen_sq_id()

    rows = []
    columns = []
    squares = []
    editable = []
    seq = []
    for i in range(9):
        rows.append([])
        columns.append([])
        squares.append([])
        editable.append([])
        seq.append([])

    for i in range(9):
        for j in range(9):
            n = list[i][j]
            if n != 0:
                rows[i].append(n)
                columns[j].append(n)
                squares[sq_id[i][j]].append(n)
                editable[i].append(1)
                seq[i].append(1)
            else:
                editable[i].append(0)
                seq[i].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

    while not verify:
        i=0

        while i < 9:
            sublist = []
            j = 0
            while j < 9:

                if list[i][j] == 0:
                    rcs = []
                    rcs.append(rows[i])
                    rcs.append(columns[j])
                    rcs.append(squares[sq_id[i][j]])

                    flat_rcs = []
                    for subrcs in rcs:
                        if len(subrcs) > 0:
                            for item in subrcs:
                                if flat_rcs.count(item) == 0:
                                    flat_rcs.append(item)

                    for item in flat_rcs:
                        try:
                            seq[i][j].remove(item)
                            if len(seq[i][j]) == 0:
                                seq[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                raise ValueError
                        except ValueError:


                            go_back = True
                            while go_back:

                                if j > 0:
                                    j -= 1
                                else:
                                    if i > 0:
                                        i -= 1
                                        j = 8
                                    else:
                                        print(1)
                                        return False



                                while editable[i][j] != 0:
                                    if j > 0:
                                        j -= 1
                                    else:
                                        if i > 0:
                                            i -= 1
                                            j = 8
                                        else:
                                            print(2)
                                            return False

                                rows[i].pop()
                                columns[j].pop()
                                squares[sq_id[i][j]].pop()
                                list[i][j] = 0
                                seq[i][j].pop(0)

                                if len(seq[i][j]) == 0:
                                    seq[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                else:
                                    go_back = False





                    n = seq[i][j][0]
                    list[i][j] = n
                    rows[i].append(n)
                    columns[j].append(n)
                    squares[sq_id[i][j]].append(n)
                    if int(time.time() - now) >= 1:
                        print(list)
                        now = time.time()
                j+=1
            i+=1
        if full_verify.check_everything(list):
            verify = True
    print(time.time()-start)
    return list

if __name__ == "__main__":
    a = []

    for i in range(9):
        a.append([int(j) for j in input().split()])

    solved = solve(a)
    if not solved:
        print(solved)
    else:
        full_verify.disp(solved)



