import os
import math
class Problem:
    def __init__(self, arr):
        self.arr = arr
        
    def calculateARow(self, i):
        values = []
        for j in range(4):
            counter = 0
            for y in range(j, j+3):
                counter += self.arr[i][y]
                counter += self.arr[i+2][y]
                if y == j+1:
                    counter += self.arr[i+1][y]
            values.append(counter)
        return values
            
    def hourglassSum(self):
        largestVal = -(math.inf)
        for i in range(4):
            rowResult = self.calculateARow(i)
            print(rowResult)
            largestRowRes = max(rowResult)
            if largestRowRes > largestVal:
                largestVal = largestRowRes
        return largestVal
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    problem = Problem(arr)
    result = problem.hourglassSum()
    fptr.write(str(result) + '\n')
    fptr.close()