class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # its finding the area of the problem 
        # we use two pointer to compare the area 

        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
                area = min(heights[l], heights[r]) * (r - l) 
                res = max(res, area)
                print(res)

                if heights[l] <= heights[r]:
                    l += 1
                else:
                    r -= 1
        
        return res

                
        # how do we ge the distance between the bars
