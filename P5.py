# Write a Python Program to swap two variable.

def swap(a,b):
    temp=a
    a=b
    b=temp
    print('\nSwaped values are :\n x = ',a,'\ny = ',b)

x=int(input('Enter x = '))
y=int(input('Enter y = '))
swap(x,y)