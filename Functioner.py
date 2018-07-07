#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

def name():
    return __name__

def doif(condition_result):
    ''' Example:
            doif([condition, function, value of the function])
        
        you can add multiple functions like that:
            doif([[condition, function, value of the function], [condition, function, value of the function], [condition, function, value of the function]])
    '''
    for i in range(0, len(condition_result)):
        if condition_result[i][0]==True:
            condition=condition_result[i][0]
            result=condition_result[i][1]
            value=condition_result[i][2]
            if value!='NoneValue':
                result(value)
            if value=='NoneValue':
                result()

def selectcolor(color):
    #turns the color into ANSII
    result = ''
    color_list = [['Black', 30], ['Default', 666], ['Red', 31], ['Green', 32], ['Yellow', 33], ['Blue', 34], ['Purple', 35], ['Cyan', 36], ['Gray', 37]]
    color_received = (color.capitalize()).strip()
    for i in range(0, len(color_list)):
        if color_received in color_list[i]:
            result = color_list[i][1]
            break
    return result

def ansii(color, bgcolor, txt):
    #Insert ANSII colors in text
    color_result = selectcolor(color)
    bgcolor_result = selectcolor(bgcolor)
    if bgcolor_result == 666:
            bgcolor_result = ''
    if bgcolor_result != '':
            bgcolor_result += 10
    return '\033[0;{};{}m{}\033[m'.format(color_result, bgcolor_result, txt)

def dialog(name, txt):
    #Simulates a dialog, like "Matt: Hi!"
    print('{}: {}'.format(name, txt))

def ClearConsole():
    #Clear the Python console
    import os
    os.system(['clear','cls'][os.name == 'nt'])


if name() == '__main__':
    ClearConsole()
    print(ansii('Black', 'Red', 'This script needs to be imported, not executed! '))
