"""
가장 흔한 단어 (https://leetcode.com/problems/most-common-word/)

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

Input:
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

Output:
    "ball"
"""
import re
import collections
import sys

class Solution:
    
    def mostCommandWord(self, paragraph: str, banned) -> str:
        # pragraph에서 문자가 아닌 부분을 ' '로 변경한다.
        words = [ word for word in re.sub('[^\w]',' ', paragraph)
            .lower().split() # 대소문자 구분이 없으므러 소문자로 변경한뒤 list
                if word not in banned] # banned에 포함되있는 문자는 포함하지 않는다.

        counts = collections.Counter(words)
        print(counts, file=sys.stderr)

        # 가장 흔하게 등장하는 단언의 첫 번쩨 인덱스 리턴
        return counts.most_common(1)[0][0]


def main():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    s = Solution()
    result = s.mostCommandWord(paragraph, banned)
    print(result)


if __name__ == "__main__":
    main()