def test1():
    test2()
    test3()


def test2():
    def test4():
        for i in range(1, 10):
            print("=========",i)
            if i == 7:
                return
    test4()

def test3():
    print("test3")
test1()
