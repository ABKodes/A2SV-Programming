class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 [:] = nums1[:m]
        nums2 = nums2[:n]
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] >= nums2[pointer2]:
                nums1.insert(pointer1, nums2[pointer2])
                pointer1 += 1
                pointer2 += 1
            else:
                pointer1 += 1
        nums1.extend(nums2[pointer2:])