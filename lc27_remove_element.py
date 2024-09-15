class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        #overcomplicated and still wrong

        # if len(nums)<2 and nums[0]!=val:
        #     return 1

        # p1 = 0
        # p2 = 1
        # while p2 < len(nums):
        #     if nums[p1]!=val:
        #         p1+=1
        #         p2+=1
        #     elif nums[p1]==nums[p2]:
        #         p2+=1
        #     else:
        #         temp = nums[p1]
        #         nums[p1] = nums[p2]
        #         nums[p2] = temp
        #         p1+=1
        #         p2+=1

        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
if __name__=="__main__":
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))