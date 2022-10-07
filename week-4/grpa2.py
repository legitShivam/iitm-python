"""
You are given a list marks that has the marks scored by a class of students in a Mathematics test. Find the median marks and store it in a float variable named median. You can assume that marks is a list of float values.

Procedure to find the median

(1) Sort the marks in ascending order. Do not try to use built-in methods. Look at the lecture 4.5 of week-4 to get a better idea.

(2) If the number of students is odd, then the median is the middle value in the sorted sequence. If the number of students is even, then the median is the arithmetic mean of the two middle values in the sorted sequence.

You do not have to accept input from the console as it has already been provided to you. You do not have to print the output to the console. Input-Output is the responsibility of the autograder for this problem. Refer to PPA-11 if you are not sure how this works.
"""
def solution(marks):
    # Sorting the list in ascending order
    for i in range(0, len(marks)):
        for i in range(0, len(marks)-1):
            if float(marks[i]) > float(marks[i+1]):
                marks[i], marks[i+1] = marks[i+1], marks[i]


    number_of_students = len(marks)
    median = float()

    # finding the median
    if number_of_students % 2 == 0:
        median = (float(marks[number_of_students//2]) + float(marks[number_of_students//2 - 1])) / 2
    else:
        median = (float(marks[number_of_students//2]))
        
    return median


# Public Test cases passed: 2/2
# Private Test cases passed: 5/5