"""
    문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

    tc1: ["h","e","l","l","o"]
    tc2: ["H","a","n","n","a","h"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1