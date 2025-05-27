class TimeMap(object):

    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.d: self.d[key] = [[value, timestamp]]
        else: self.d[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """ 
        value = ""

        if key not in self.d: return value
        values = self.d[key]

        l_ptr, r_ptr = 0, len(values) - 1
        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr)//2
            if values[mid][1] <= timestamp:
                value = values[mid][0]
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        return value

if __name__ == "__main__":

    try:
        ip = []
        op = []

        with open(r"LEETCODE\0981 - Time Based Key-Value Store\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    ip.append(line.split(": ")[-1])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        print("\nInput:", ip[0])
        print("Expected Output:", op[0])
        obj = TimeMap()
        gop = [None, obj.set("foo", "bar", 1), obj.get("foo", 1), obj.get("foo", 3), obj.set("foo", "bar2", 4), obj.get("foo", 4), obj.get("foo", 5)]
        print("Generated Output:", gop)
        print()

    except Exception as e:
        print(e)
        pass