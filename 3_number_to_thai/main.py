"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def __init__(self):
        self.units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        self.tens = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        
    def validate_input(self, number):
        if not isinstance(number, int):
            return False, "input is not a valid number"
        if number < 0:
            return False, "number can not be less than 0"
        return True, None
    
    def is_zero(self, number):
        if number == 0:
            return True, "ศูนย์"
        return False, None

    def number_to_thai_text(self, number):
        is_valid, error_message = self.validate_input(number)
        if not is_valid:
            return error_message
        
        is_zero, zero_text = self.is_zero(number)
        if is_zero:
            return zero_text

        num_text = ''
        num_str = str(number)
        length = len(num_str)

        for i in range(length):
            digit = int(num_str[i])
            position = length - i - 1

            if digit == 0:
                continue

            if position == 1 and digit == 2:
                num_text += "ยี่"
            elif position == 1 and digit == 1:
                if i == 0 or (i > 0 and num_str[i - 1] != '0'):
                    num_text += "สิบ"
                else:
                    num_text += "เอ็ด"
            elif position == 0 and digit == 1 and length > 1:
                num_text += "เอ็ด"
            else:
                num_text += self.units[digit]

            if digit != 0:
                num_text += self.tens[position]

        return num_text


solution = Solution()

print(solution.number_to_thai_text(1234567))
print(solution.number_to_thai_text(0))
        
        
        
        
            
        
