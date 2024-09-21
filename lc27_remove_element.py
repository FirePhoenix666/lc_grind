class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        pointer1 = 0
        for pointer2 in range(0, len(nums)):
            if nums[pointer2]!=val:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer1 += 1
        return pointer1

    
if __name__=="__main__":
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
    # print(Solution().removeElement([3,2,2,3, 3, 3, 2], 3))