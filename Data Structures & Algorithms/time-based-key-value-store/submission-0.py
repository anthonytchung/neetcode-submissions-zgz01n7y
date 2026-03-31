class TimeMap:

    def __init__(self):
        self.obj = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.obj:
            self.obj[key] = []
        self.obj[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        array = self.obj.get(key, [])
        print(array)

        l, r = 0, len(array)-1
        while l <= r:
            half = l + ((r-l) // 2)

            if array[half][0] <= timestamp:
                res = array[half][1]
                l = half + 1
            else:
                r = half -1



        return res
        
