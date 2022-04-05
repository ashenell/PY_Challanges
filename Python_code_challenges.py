
"""
from math import pi
#Convert radians into degrees

instert_radian = ''
while instert_radian is not int:
    try:
        instert_radian = int(input('Enter numeric radian value: '))
        break
    except ValueError:
        print('Value is not correct!')
            
calca = instert_radian * (180 / pi)

print(calca) #Test
"""
