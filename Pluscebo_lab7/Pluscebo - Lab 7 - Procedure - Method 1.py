# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 08:23:49 2024

@author: Cj Carag
"""

#TUI Form
def main():
# Find the largest number among three numbers
 L = []
 num1 = eval(input("Enter the first number:"))
 L.append(num1)
 num2 = eval(input("Enter the second number:"))
 L.append(num2)
 num3 = eval(input("Enter the third number:"))
 L.append(num3)
 print("The largest number among the three is:",str(max(L)))
main()  