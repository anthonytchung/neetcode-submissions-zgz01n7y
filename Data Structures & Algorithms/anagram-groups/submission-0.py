class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for string in strs:
            if str(sorted(string)) in found:
                found[str(sorted(string))].append(string)
            else:
                found[str(sorted(string))] = [string]

        # bigList = [[] for i in range(len(found))]
        # for vec in bigList:
        #     vec = found.v
        return found.values()

        
