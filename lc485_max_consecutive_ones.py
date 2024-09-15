class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        
        sum = 0
        max_sum = 0

        for i in nums:
            if i == 0:
                if sum > max_sum:
                    max_sum = sum
                sum = 0
            else:
                sum+=1
        if sum > max_sum:
            max_sum=sum
        return max_sum

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))