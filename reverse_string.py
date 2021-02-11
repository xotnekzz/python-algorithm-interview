"""
문자열 뒤집기 ( https://leetcode.com/problems/reverse-string/ )

문자열을 뒤집는 함수를 작성하라, 입력값을 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

Input :
    ["h","e","l","l","o"]

Output : 
    ["o","l","l","e","h"]
"""
import sys


def reverseString_1(s):
    """
    투 포인터를 이용한 스왑
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)
    

def reverseString_2(s):
    """
    Pythonic Down (파이썬 다운 방식)
    """
    s.reverse()
    print(s)


def reverseString_3(s):
    """
    Pythonic Down (파이썬 다운 방식)
    """
    s = s[::-1]
    print(s)


def main():
    s = ["h","e","l","l","o"]
    reverseString_1(s)
    reverseString_2(s)
    reverseString_3(s)


if __name__ == "__main__":
    main()