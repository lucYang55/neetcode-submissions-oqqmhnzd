class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # there shoukd be two ways to do this one way is using a dict itarating through
        # and or use two pointer
        # if we want o(1) space then we have to two pointer it

        l, r = 0, len(numbers) - 1
        print(r)

        while l <= r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1


    