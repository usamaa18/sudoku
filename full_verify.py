def check (test):
    for i in range(1,10,1):
        if test.count(i) != 1:
            return False
    return True


def check_everything (a):
    # row check
    for test in a:
        if check(test) == False:
            return False

    # column check
    for i in range(9):
        test = []
        for j in range(9):
            test.append(a[j][i])
        if check(test) == False:
            return False

    # 3x3 square check
    for i in range(0,7,3):
        test = []
        count = 0
        for j in range(9):
            test.append(a[j][i:i+3])
            count += 1
            if count == 3:

                # flatten the 2d list test
                flat_test = []
                for sublist in test:
                    for item in sublist:
                        flat_test.append(item)

                if check(flat_test) == False:
                    return False
                test = []
                count = 0

    return True


def disp(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()


if __name__ == "__main__":
    a = []

    for i in range(9):
        a.append([int(j) for j in input().split()])



    print (check_everything(a))