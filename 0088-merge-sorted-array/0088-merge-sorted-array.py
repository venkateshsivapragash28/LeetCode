class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = (nums1[:m] + nums2[:n])
        for i in range(1, len(nums1)):
            for j in range(i, 0, -1):
                if nums1[j-1] > nums1[j]:
                    nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
        return nums1