class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        l = n + m
        if l & 1:
            return findKSmallest(nums1, nums2, (l + 1) / 2)
        else:
            return (findKSmallest(nums1, nums2, l / 2 + 1) + findKSmallest(nums1, nums2, l / 2)) / 2.0


def findKSmallest(nums1, nums2, k):
    n = len(nums1)
    m = len(nums2)
    if n > m:
        return findKSmallest(nums2, nums1, k)
    if n == 0:
        return nums2[k]
    if k == 1:
        return min(nums1[0], nums2[0])
    pa = min(k / 2, n)
    pb = k - pa
    if nums1[pa - 1] > nums2[pb - 1]:
        return findKSmallest(nums1, nums2[pb:], k - pb)
    elif nums1[pa - 1] < nums2[pb - 1]:
        return findKSmallest(nums1[pa:],nums2,k-pa )
    else:
        return nums1[pa - 1]