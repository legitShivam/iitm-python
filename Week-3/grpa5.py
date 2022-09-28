"""
Accept a phone number as input. A valid phone number should satisfy the following constraints.

(1) The number should start with one of these digits: 6, 7, 8, 9

(2) The number should be exactly 10 digits long.

(3) No digit should appear more than 7 times in the number.

(4) No digit should appear more than 5 times in a row in the number.

If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string valid if the phone number is valid. If not, print the string invalid.
"""

phone_number = input()

flag = True

if phone_number[0] not in "6789":
    flag = False
elif len(phone_number) != 10:
    flag = False
        
for i in range(10):
    if phone_number.count(str(i)) > 7:
        flag = False
        break
    elif str(i)*6 in phone_number:
        flag = False
        break 
    
    
if flag:
    print("valid", end="")
else:
    print("invalid", end="")
    

# Public Test cases passed: 3/3
# Private Test cases passed: 5/5

