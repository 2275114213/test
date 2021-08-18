visted = set()


def bfs(graph, start, end):
    queue = []
    queue.append(start)
    visted.add(start)
    while queue:
        # 删除第一个
        node = queue.pop(0)
        visted.add(node)
        process(node)
        nodes = generate_relate_nodes(nodes)
        queue.append(nodes)


def BFS(graph, s):
    queue = []
    queue.append(s)
    visted.add(s)
    while len(queue):
        node = queue.pop(0)
        nodes = graph[node]
        for w in nodes:
            if w not in visted:
                queue.append(w)
                visted.add(w)
        print(node)
