class Solution(object):
    def majorityElement(self, arr):
        nums = []
        counter = {}
        if nums is None:
            return 0
        for i in arr:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i]+=1


        for i in arr:
            if counter[i] > len(arr)/3:
                nums.append(i)
        return list(set(nums))