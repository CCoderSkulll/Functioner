#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import os

def name():
    #Just a function to simplify __name__ to name()
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
    '''turns the color into ANSII numbers (add + 10 if it's background)
        Example:
            selectcolor('Black')
        
        --Remember--
            if you want a text with ANSII, see the ansii function.
    '''
    result = ''
    color_list = [['Black', 30], ['Default', 666], ['Red', 31], ['Green', 32], ['Yellow', 33], ['Blue', 34], ['Purple', 35], ['Cyan', 36], ['Gray', 37]]
    color_received = (color.capitalize()).strip()
    for i in range(0, len(color_list)):
        if color_received in color_list[i]:
            result = color_list[i][1]
            break
    return result

def ansii(color, bgcolor, txt):
    '''Insert ANSII colors in text
        (See selectcolor() to know the colors you can use)
    '''    
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
    os.system(['clear','cls'][os.name == 'nt'])

def src(TypeSrc, src):
    '''
        Types of search{
            "web" (Website search);
            "yt" (Youtube search);
            "gg" (Google search);
        }
    '''
    import webbrowser
    src_configured = src.strip()
    src_types = [['web', 'https://', ''], ['yt', 'https://www.youtube.com/results?search_query=', '+'], ['gg', 'https://www.google.com/#q=', '+']]
    for i in range(0, len(src_types)):
        if TypeSrc == src_types[i][0]:
            url=src_types[i][1]
            ind = i
    for i in range(0, len(src_configured)):
        if src_configured[i]==' ':
            url+=src_types[ind][2]
        if src_configured[i]!=' ':
            url+=src_configured[i]
    url=url.strip()
    webbrowser.open(url)
class MiniWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('550x130+450+280')
    def InterfaceInput(self, txt):
        self.txt = str(txt)
        self.reset()
        self.answer = tkinter.Entry(self.window, width=30)
        question = tkinter.Label(self.window, width=20, text=str(self.txt))
        confirm_button = tkinter.Button(self.window, width=20, text="Ok", command=self.Capture_Input)
        question.pack()
        self.answer.pack()
        self.answer.focus()
        confirm_button.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.Repeat_Input)
        self.window.resizable(False, False)
        self.window.mainloop() 
        return self.final_answer
    def Repeat_Input(self):
        self.InterfaceInput(self.txt)
    def Capture_Input(self):
        self.final_answer = (self.answer).get()
        self.window.quit()
    def reset(self):
        self.window.destroy()
        self.__init__()
if name() == '__main__':
    #If the script is executed, do that:
    ClearConsole()
    print(ansii('Black', 'Red', 'This script needs to be imported, not executed! '))