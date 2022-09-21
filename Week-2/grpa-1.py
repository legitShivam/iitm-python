# Accept three positive integers as input and check if they form the sides of a right triangle. Print YES if they form one, and NO if they do not. The input will have three lines, with one integer on each line. The output should be a single line containing one of these two strings: YES or NO.

side1 = int(input())
side2 = int(input())
side3 = int(input())

# checking if the sides form a right triangle
if side1 ** 2 + side2 ** 2 == side3 ** 2 or side1 ** 2 + side3 ** 2 == side2 ** 2 or side2 ** 2 + side3 ** 2 == side1 ** 2:
    print("YES", end='')
else:
    print("NO", end='')

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5