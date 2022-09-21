"""
Accept a string as input. Your task is to determine if the input string is a valid password or not. For a string to be a valid password, it must satisfy all the conditions given below:

(1) It should have at least 8 and at most 32 characters
(2) It should start with an uppercase or lowercase letter
(3) It should not have any of these characters: / \ = ' "
(4) It should not have spaces

It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). Output True if the string forms a valid password and False otherwise.
"""

password = input()

flag = True

if not (8 <= len(password) <= 32):
    flag = False
elif not (password[0].isalpha()):
    flag = False
elif ' ' in password:
    flag = False
else:
    for i in password:
        if i in ['/', '\\', '=', "'", '"']:
            flag = False
            break

print(flag, end='')

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5