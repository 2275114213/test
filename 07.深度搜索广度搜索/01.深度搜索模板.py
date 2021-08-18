visited = set()


# 递归
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

        return func3()

    func2()
    return


graph = {"A": ["B", "C"]}


# A 的临近结点为B和C


# 迭代
def DFS(graph, s):
    stack = []
    stack.append(s)
    visited = set()
    while (len(stack)):
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(s)
        nodes = graph[vertex]
        for w in nodes:
            if w not in visited:
                stack.append(w)
        print(vertex)


res = fun1()
print(res)
