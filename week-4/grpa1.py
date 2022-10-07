"""
In the first line of input, accept a sequence of space-separated words. In the second line of input, accept a single word. If this word is not present in the sequence, print NO. If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.

"""

str = input().split(" ")
word = input()

if word in str:
    print("YES")
    count = 0
    for i in range(len(str)):
        if str[i] == word:
            count += 1
    print(count, end="")
else:
    print("NO", end="")

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5