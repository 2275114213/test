import collections


class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)  # OrderedDict([('test', 'dsds'), ('test1', 'dsds'), ('test2', 'dsds')])
        self.dic[key] = v  # key as the newest one 
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value


LRUCacheD = LRUCache(2)
LRUCacheD.put(1, 1)  # 缓存是 {1=1}
LRUCacheD.put(2, 2)  # 缓存是 {1=1, 2=2}
LRUCacheD.get(1)  # 返回 1
LRUCacheD.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
LRUCacheD.get(2)  # 返回 -1 (未找到)
LRUCacheD.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
LRUCacheD.get(1)  # 返回 -1 (未找到)
LRUCacheD.get(3)  # 返回 3
LRUCacheD.get(4)  # 返回 4

lru = LRUCache(3)
lru.put("test", "dsds")
lru.put("test1", "dsds")
lru.put("test2", "dsds")
res = lru.get("test1")
print(lru.dic)
print(res)
