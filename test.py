def test1():
    test2()
    test3()


def test2():
    def test4():
        for i in range(1, 10):
            print("=========", i)
            if i == 7:
                return

    test4()


def test3():
    print("test3")


test1()

dp = [[0] * (10 + 1) for _ in range(4)]

f = [[1] * 3] + [[1] + [0] * (3 - 1) for _ in range(9- 1)]

print(f)
