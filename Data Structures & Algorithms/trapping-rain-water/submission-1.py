class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        res = 0

        if not height:
            return 0

        while l < r:
            # we need to take the min of the two MAX
            if leftMax < rightMax:
                l += 1
                # increment the left to move the pointer 
                # calculate the new max with leftmax and the current element
                leftMax = max(leftMax, height[l])
                # add to the res with the heights 
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res 
