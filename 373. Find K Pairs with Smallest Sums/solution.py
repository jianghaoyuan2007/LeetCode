import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        pairs = []
        for num1 in nums1:
            for num2 in nums2:
                pairs.append([num1, num2])
        return heapq.nsmallest(k, pairs, key=lambda s: s[0] + s[1])

