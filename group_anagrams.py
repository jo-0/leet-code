# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/


from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    hashmap = {}
    result = []
    for string in strs:
        string = "".join(sorted(string))
        hashmap[string] = hashmap.get(string, 0) + 1

    for string in strs:
        sortedString = "".join(sorted(string))
        if sortedString in hashmap and hashmap[sortedString] > 1:
            result.append(string)

    return result


print("Group = ", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
