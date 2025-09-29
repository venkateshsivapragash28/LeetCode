class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            output[key].append(i)

        return list(output.values())