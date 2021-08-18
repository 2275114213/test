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
