class Solution:
    def intersection(self, nums1, nums2):
        if not nums1 or len(nums1) == 0 or not nums2 or len(nums2) == 0:
            return []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        count = min(len(nums1), len(nums2))
        result = []
        index = 0
        if len(nums1) < len(nums2):
            long_list = nums2
            short_list = nums1
        else:
            long_list = nums1
            short_list = nums2
        while index < count:
            value = short_list[index]
            for num in long_list:
                if num == value:
                    result.append(value)
                    break
            index += 1
        return result

