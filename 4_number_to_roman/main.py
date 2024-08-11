"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def __init__(self):
        self.val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not be less than 0"
        if number == 0:
            return "N"  # Roman numerals do not have a representation for 0; "N" (nulla) was used in the Middle Ages.

        roman_text = ""
        for value, symbol in self.val_map:
            while number >= value:
                roman_text += symbol
                number -= value
        return roman_text
    
sol = Solution()

for i in range(1, 102):
    print(sol.number_to_roman(i))
