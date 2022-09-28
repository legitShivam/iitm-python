"""
A bot starts at the origin — (0, 0)(0,0) — and can make the following moves:

(1) UP
(2) DOWN
(3) LEFT
(4) RIGHT
Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input. The first entry in the sequence is always START while the last entry in the sequence is always STOP. A sample sequence is given below:

START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP

Print the Manhattan distance of the bot from the origin. If the bot is at the position (x, y)(x,y), then its Manhattan distance from the origin is given by the equation:

D = |x| + |y|D=∣x∣+∣y∣
"""

# Reading moves from user
moves = ['']
while moves[-1] != "STOP":
    moves.append(input())

# Calculating x and y coordinates
x = 0
y = 0

for i in moves:
    if i == "UP":
        y += 1
    elif i == "DOWN":
        y -= 1
    elif i == "LEFT":
        x += 1
    elif i == "RIGHT":
        x -= 1
        
# Calculating Manhattan distance
manhattan_distance = abs(x) + abs(y)
print(manhattan_distance, end="") 

# Public Test cases passed: 2/2
# Private Test cases passed: 5/5