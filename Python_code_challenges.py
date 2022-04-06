
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
'''
Deciamal numbers to binary numbers converter
def decimal_binary(val):
    if val >= 1:
       decimal_binary(val // 2)
    print(val % 2, end='')

decimal_binary(23)
'''
'''
#Find equal vowels y is not
def vowels():
    word = 'konnlakskraavi'
    words = [['a'], ['e'], ['i'], ['o'], ['u']]
    empty = []
    for x in range(0, len(word)):
        empty.append([word[x]])
    for xa in empty:
        for xu in words:
            if xu == xa:
                print('equal', xa)
vowels()
'''
'''
#Hide credit card digit numbders show only last 4 numbers
def credit_card(self):
    print(str(self)[-4:].rjust(len(str(self)), "*"))   
credit_card(1234567890123456)
'''
