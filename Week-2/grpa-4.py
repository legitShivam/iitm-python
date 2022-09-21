"""
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order.
The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
"""

import datetime

# reading details of Person 1
person1 = input()
dob1 = datetime.datetime.strptime(input(), '%d-%m-%Y')

# reading details of Person 2
person2 = input()
dob2 = datetime.datetime.strptime(input(), '%d-%m-%Y')

# comparing the dates of birth
younger = ''
if dob1 > dob2:
    younger = person1
elif dob1 < dob2:
    younger = person2
elif person1 < person2:
    younger = person1
else:
    younger = person2

# Printing the name of the younger person
print(younger, end='')

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5