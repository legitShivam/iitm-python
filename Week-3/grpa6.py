"""
Accept a positive integer nn as input and print a "number arrow" of size nn. For example, n = 5n=5 should produce the following output:

1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1

You can assume that n \geq 2n≥2 for all test cases.
"""

n = int(input())

for i in range(1, n+1):
    print(",".join([str(j) for j in range(1, i+1)]))
for i in range(n-1, 0, -1):
    print(",".join([str(j) for j in range(1, i+1)]))
    
# Public Test cases passed: 2/2
# Private Test cases passed: 5/5