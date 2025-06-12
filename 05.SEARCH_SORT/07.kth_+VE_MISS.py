class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        miss = []

        max_ele = arr[-1]

        for i in range(1, max_ele):  # Start from 1, not 0
            if i not in arr:
                miss.append(i)

        i = max_ele
        while len(miss) < k:
            i += 1
            if i not in arr:
                miss.append(i)

        return(miss[k - 1])  # Index should be k-1, not k
