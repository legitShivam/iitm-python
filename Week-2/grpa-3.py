# Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output. Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.

string = input().lower()
vowel = []

for i in string:
    if i in ['a','e','i','o','u']:
        vowel.append(i)

if vowel == []:
    print("none", end='')
else:
    vowel = list(set(vowel))
    vowel.sort()
    for i in vowel:
        print(i, end='')

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5