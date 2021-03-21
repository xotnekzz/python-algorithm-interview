"""
그룹 애너그램 (https://leetcode.com/problems/group-anagrams/)

Input:
    ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
    ["ate","eat","tea"]
    ["tan","nat"]
    ["bat"]
"""
import collections


class Solution:

    def group_anagram(self, iplist):
        """
        리스트의 요소들을 정렬을 해서, 같은 요소들을 묶어서 리턴
        """
        anagrams = collections.defaultdict(list)

        for word in iplist:
            # 정렬하여 딕셔너리에 추가
            # sorted(str) "test" -> ["e","s","t","t"] 문자열도 정렬 가능
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


def main():
    iplist = ["eat", "tea", "tan", "ate", "nat", "bat"]

    s = Solution()

    result = s.group_anagram(iplist)
    


if __name__ == "__main__":
    main()