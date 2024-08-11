"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int:
        if not numbers:
            return "list can not blank"
        
        max_number = max(numbers)
        max_index = numbers.index(max_number)
        return max_index
    
sol = Solution()
print(sol.find_max_index([1,2,1,3,5,6,4]))
print(sol.find_max_index([]))
        
        
