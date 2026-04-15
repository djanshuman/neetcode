from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dictmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictmap[key].append([timestamp, value])

        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictmap:
            return ""
        
        pos = -1
        l   = 0
        r   = len(self.dictmap[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.dictmap[key][mid][0] <= timestamp:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1

        if pos != -1:
            return self.dictmap[key][pos][1]
        else:
            return ""
        
