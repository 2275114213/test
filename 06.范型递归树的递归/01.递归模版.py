def recursion(level, param1, param2, param3):
    if level > MAX_LEVEL:  # 递归终结条件
        process_result
        return
    process(level, data)  # 处理当前层逻辑

    recursion(level + 1, p1, p2, p3) # 下探到下一层

    # 清理当前层