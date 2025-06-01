#Given int 'n' by User
#if 'n' is odd Print "Weird"
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

#Input Format:
#A single line containing a positive integer, n.

#Constraints:
#1<=n<=100

#Output Format:
#Print Weird if the number is weird. Otherwise, print Not Weird.

#MY SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print("Enter a number")#can remove this print statement if HackerRank is giving error.
    n = int(input().strip())
    if n%2==1:
       print("Weird")
    elif 2<n<=5:
        print("Not Weird")
    elif 5<n<=20:
        print("Weird")
    else:
        print("Not Weird")
