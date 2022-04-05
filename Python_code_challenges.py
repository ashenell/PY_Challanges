
"""

from math import pi
def function_conver():
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
functuin_convert()
"""
'''
#Sort a list to asc/desc if input does not meat the value it prints out lists
def function_sort():
    list_nums = [5, 6, 7 ,4 ,8 ,9 , 1, 3] #Store list of random numbesrs
    values = ''
    value1 = 'asc'
    value2 = 'desc'
    value3 = 'none'
    values = input('How you wanna sort the list(asc)(desc)(none): ')

    if values == value1:
        list_nums.sort()
        print(list_nums)
    elif values == value2:
        list_nums.sort(reverse=True)
        print(list_nums)
    else:
        print(list_nums)    
function_sort()   
'''
