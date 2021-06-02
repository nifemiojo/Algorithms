class Solution:
    # O(n^2) solution
    # Runtime - 8880 ms
    def twoSum_slow(self, nums, target):
        for (x, y) in enumerate(nums):
            for (i, j) in enumerate(nums):
                if x != i and y + j == target:
                    return [x, i]

    def twoSum_slowv2(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums), 0, -1):
                if i >= j - 1:
                    break
                elif nums[i] + nums[j - 1] == target:
                    return [i, j - 1]

    # Runtime - 180ms
    def twoSum_myoriginal(self, nums, target):
        # O(n log n) in python
        new_nums = sorted(nums)

        for j in range(len(nums), 0, -1):
            for i in range(len(nums)):
                if new_nums[j - 1] + new_nums[i] == target:
                    first = nums.index(new_nums[i])
                    if new_nums[j - 1] == new_nums[i]:
                        second = nums.index(new_nums[j - 1], first + 1)
                    else:
                        second = nums.index(new_nums[j - 1])
                    return [first, second]
                elif new_nums[j - 1] + new_nums[i] > target or \
                        new_nums[i] == new_nums[j - 1] or i >= j:
                    break

    def twoSum(self, nums, target):
        seen = {}  # {value: index}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([3, 2, 4], 6)
    print(res)
