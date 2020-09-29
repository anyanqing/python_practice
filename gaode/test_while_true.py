import timeit

def test_while_1():
    i = 0
    while 1:
        i += 1
        if i < 1000000000:
            continue
        else:
            break


def test_while_true():
    i = 0
    while True:
        i += 1
        if i < 1000000000:
            continue
        else:
            break


if __name__ == '__main__':
    w1 = timeit.timeit(test_while_1, number=3)
    w2 = timeit.timeit(test_while_true, number=3)
    print(w1, w2)  # 161.7610688 172.9623908


