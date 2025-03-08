class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            grouped = False
            for key in dic.keys():
                if len(s)!=len(key):
                    continue
                equivalent = True
                for c in s:
                    if s.count(c)==key.count(c):
                        continue
                    else:
                        equivalent = False
                        break
                if equivalent:
                    dic[key].append(s)
                    grouped = True
                    break
            if not grouped:
                dic[s] = [s]
        # create final list
        groups = []
        for s in dic.keys():
            groups.append(dic[s])
        return groups
        