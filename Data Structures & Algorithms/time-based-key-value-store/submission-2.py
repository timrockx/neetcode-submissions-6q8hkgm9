import bisect
class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        
        idx = -1
        if key in self.store:
            values = self.store[key]

            left, right = 0, len(values) - 1            
            while left <= right:
                mid = (left + right) // 2
                if values[mid][0] <= timestamp:
                    idx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
        return values[idx][1] if idx != -1 else ""
        