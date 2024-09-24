class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # forward = []
        # backward = []
        # output = nums
        # len_ = len(nums)

        # temp = 1
        # for num in nums:
        #     temp = temp*num
        #     forward.append(temp)

        # temp = 1
        # for num in nums[::-1]:
        #     temp = temp*num
        #     backward.append(temp)
        
        # output[0] = backward[-2]
        # output[-1] = forward[-2]

        # for idx in range(1, len_-1):
        #     output[idx] = forward[idx-1]*backward[len_-2-idx]

        output = [1 for i in range (0, len(nums))]

        temp = 1
        for i in range(1, len(nums)):
            temp = nums[i-1]*temp
            output[i] = temp

        temp = 1
        for j in range(len(nums)-2, -1, -1):
            temp = temp*nums[j+1]
            output[j] = output[j]*temp
        
        return output


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    #[-1,1,0,-3,3]
    output = Solution().productExceptSelf(nums=nums)
    print(output)
        