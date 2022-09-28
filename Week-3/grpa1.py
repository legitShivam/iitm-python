"""
Accept a positive integer n as input and print the sum of the first n terms of the series given below: 
1+(1+2)+(1+2+3)+(1+2+3+4)+⋯
Just to be clear, the first term in the series is 11, the second term is (1 + 2)(1+2) and so on.
"""

n = int(input())

sum = 1
for i in range(2, n+1):
    temp = sum
    sum += (i*(i+1)/2)
    
print(int(sum), end="")

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5
