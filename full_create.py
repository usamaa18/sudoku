import full_verify
import random
import time # takes around 90ms for each sudoku

def reduce(x):
    index = 0
    if x <= 2:
        index = 0
    elif x <= 5:
        index = 1
    elif x <= 8:
        index = 2
    return index

def gen_sq_id():
    sq_id = []
    for i in range(9):
        sub = []
        for j in range(9):

            indexj = reduce(j)
            indexi = reduce(i)

            value = indexj + (3*indexi)
            sub.append(value)
        sq_id.append(sub)
    return sq_id

def generate():

    random.seed()

    count = 0
    sudoku_count = 0

    sq_id = gen_sq_id()

    n=0
    #start_time = time.time()

    verify = False
    while not verify:

        rows = []
        columns = []
        squares = []

        for i in range(9):
            rows.append([])
            columns.append([])
            squares.append([])


        list = []
        for i in range(9):
            sublist = []
            for j in range(9):
                seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                duplicate = True
                rcs = []
                rcs.append(rows[i])
                rcs.append(columns[j])
                rcs.append(squares[sq_id[i][j]])

                # flatten the 2d list rcs
                flat_rcs = []
                for subrcs in rcs:
                    if len(subrcs)>0:
                        for item in subrcs:
                            if flat_rcs.count(item) == 0:
                                flat_rcs.append(item)

                for item in flat_rcs:
                    try:
                        seq.remove(item)
                    except ValueError:
                        pass

                n = 0
                if len(seq) == 0:
                    print("no elements")
                    break

                n = random.choice(seq)

                if n == 0:
                    break




                rows[i].append(n)
                columns[j].append(n)
                squares[sq_id[i][j]].append(n)

                sublist.append(n)
            if n == 0:
                break
            list.append(sublist)



        count += 1


        if n == 0:
            verify = False
        elif full_verify.check_everything(list):
            verify = True
            #full_verify.disp(list)
            #sudoku_count += 1
            #print(sudoku_count)

        #if sudoku_count == 100:
        #    verify = True
    print(count)
    return list
    #print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    list = generate()
    full_verify.disp(list)