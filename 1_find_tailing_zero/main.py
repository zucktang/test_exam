"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def is_positive(self, number):
        if number < 0:
            return False, "number can not be negative"
        return True, None
        
    def find_tailing_zeroes(self, number: int) -> int:
        is_positive, error_message = self.is_positive(number)
        if not is_positive:
            return error_message
        
        count = 0
        i = 5
        while number >= i:
            count += number // i
            i *= 5
        return count
    
sol = Solution()
print(sol.find_tailing_zeroes(7))
print(sol.find_tailing_zeroes(-1))
print(sol.find_tailing_zeroes(100))
        
