"""
유효한 팰린드롬 ( https://leetcode.com/problems/valid-palindrome/ )

palindrome : 앞뒤가 똑같은 단어나 문장을, 뒤집어도 같은 말이 되는 단어 또는 문장을 팰림드롬이라 한다.

Input : A man, a plan, a canal: Panama

Output : true
"""
import sys
import collections
import re


def isPalindrome_1(s):
    """리스트 풀이
    """
    strs = []
    for char in s:
        if char.isalnum(): # isalnum() -> 문자(char)가 영문자, 숫자인지 판별해주는 함수. 
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def isPalindrome_2(s):
    """데크 자료형을 이용한 최적화

    list 사용시에 O(n)으로 탐색하지만,
    Deque를 사용하면 O(1)로 탐색이 가능하다.
    """
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
        
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
        
    return True


def isPalindrome_3(s):
    """슬라이싱 사용
    
    [::-1] 사용

    """
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s) # 영어와 숫자만 필터링
    return s == s[::-1] # 슬라이싱 
     

def main():
    s = sys.argv[1]
    print(isPalindrome_1(s))        
    print(isPalindrome_2(s))        
    print(isPalindrome_3(s))        


if __name__ == "__main__":
    main()