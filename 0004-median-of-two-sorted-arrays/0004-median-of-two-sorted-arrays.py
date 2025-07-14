class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sorted = nums1 + nums2
        sorted.sort()
        if len(sorted)%2 != 0:
            y = (len(sorted)//2)
            return (sorted[y])
        else:
            x = (len(sorted)//2)-1
            y = (len(sorted)//2)
            ans = sorted[x]+sorted[y]

            return ans/2.0