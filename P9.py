# Write a Python program to display calendar.

import calendar
def dis(yy,mm):
    print(calendar.month(yy,mm))

yy = int(input("Enter year: "))  
mm = int(input("Enter month: ")) 
dis(yy,mm)
