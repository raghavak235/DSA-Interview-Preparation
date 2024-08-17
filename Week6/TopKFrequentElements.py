# https://leetcode.com/problems/top-k-frequent-elements/

# Time Complexity: O(logn)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        dict1 = Counter(nums)
        print(dict1)
        return heapq.nlargest(k, iterable=dict1.keys(), key=dict1.get)