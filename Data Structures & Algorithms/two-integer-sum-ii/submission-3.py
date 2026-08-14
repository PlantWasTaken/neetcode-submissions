class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lPtr = 0
        rPtr = len(numbers)-1
        print(len(numbers), numbers[0])

        for _ in range(len(numbers)):
            n = numbers[lPtr] + numbers[rPtr]
            if(n == target):
                return [lPtr+1, rPtr+1]
            if(n > target):
                rPtr -= 1
            if(n < target):
                lPtr += 1
        return [lPtr+1, rPtr+1]
