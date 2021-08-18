visited = set()


def dfs(node, visted):
    if node in visted:
        return
    visted.add(node)
    for next_node in node.children():
        if next_node not in visted:
            dfs(next_node, visted)


def fun1():
    def func2():
        def func3():
            return "fun3"

        func3()
        return "func2"

    func2()
    return "func1"


res = fun1()
print(res)
