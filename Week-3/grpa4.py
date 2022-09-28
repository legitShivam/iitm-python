"""
Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
"""

# Reading string from user and converting it to lower case and sorting it
string = sorted(input().lower())
string = "".join(string)

# Printing the sorted string
print(string, end="")

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5