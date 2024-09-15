class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        pointer1 = 0

        for pointer2 in range(1, len(nums), 1):
            if nums[pointer1]!=nums[pointer2]:
                pointer1+=1
                nums[pointer1]=nums[pointer2]
        return pointer1+1

if __name__ == "__main__":
    nums = [1,1,2]
    output = Solution().removeDuplicates(nums=nums)
    print(output)