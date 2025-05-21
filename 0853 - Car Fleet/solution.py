class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [(position[i], speed[i]) for i in range(len(position))]
        closest_cars = sorted(cars, reverse = True)
        stack = []
        for car in closest_cars:
            time_needed = (target - car[0])/car[1]
            if not stack or stack[-1] < time_needed:
                stack.append(time_needed)
        return len(stack)
        
if __name__ == "__main__":
    
    try:
        ip = []
        op = []

        with open(r"LEETCODE\0853 - Car Fleet\test.txt") as f:
            line = f.readline()
            while line:
                if "Input" in line:
                    target_str, position_str, speed_str = line.split(", ")
                    position_str = position_str.split()[-1]
                    speed_str = speed_str.split()[-1]
                    position_list = [int(i) for i in position_str[1:-1].split(",")]
                    speed_list = [int(i) for i in speed_str[1:-1].split(",")]
                    target = int(target_str.split()[-1])
                    ip.append([target, position_list, speed_list])
                elif "Output" in line:
                    op.append(line.split()[-1])
                line = f.readline()

        soln = Solution()
        for i in range(len(ip)):
            print("\nInput:", ip[i][0], ip[i][1], ip[i][2])
            print("Expected Output:", op[i])
            print("Generated Output:", soln.carFleet(ip[i][0], ip[i][1], ip[i][2]))
        print()

    except Exception as e:
        print(e)
        pass