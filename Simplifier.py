#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import os
import time
import random

def doIf(condition_result):
    ''' Example:
            doIf([condition, function, value of the function])
        
        you can add multiple functions like that:
            doIf([[condition, function, value of the function], [condition, function, value of the function], [condition, function, value of the function]])
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

def selectColor(color):
    '''turns the color into ANSII numbers (add + 10 if it's background)
        Example:
            selectColor('Black')
        
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
        (See selectColor() to know the colors you can use)
    '''    
    color_result = selectColor(color)
    bgcolor_result = selectColor(bgcolor)
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
    #Search on the web with this function!
    search_types = [
            "web",
            "yt",
            "gg",
        ]
    if TypeSrc in search_types:
        import webbrowser
        src_configured = src.strip()
        src_types = [['web', 'https://', ''], ['yt', 'https://www.youtube.com/results?search_query=', '+'], ['gg', 'https://www.google.com/search?q=', '+']]
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
    else:
        print('Invalid type of search! ')
        print('Only these are valids: {}!'.format(search_types))

def splitWords(txt, exceptions):
    #Splits the words of the given text
    '''If you want to disconsider some kind of letter,
        put them in the exceptions.
    '''
    txt = (str(txt)).strip()+' '
    words = []
    word_to_add=''
    for i in txt:
        if i==' ':
            words.append(word_to_add)
            word_to_add=''
        else:
            if not i in exceptions or exceptions=='none':    
                word_to_add+=i
    return words

def breakLine(txt):
    #Automatically break the lines
    splitted_txt = splitWords(txt, 'none')
    quant_words = 0
    text=''
    for word in splitted_txt:
        quant_words += 1
        text += ' {}'.format(word)
        if len(word)>10 or quant_words%3==0:
            text+='\n'  
    return text

def printClearing(txt):
    #Clear the Console while printing the txt
    ClearConsole()
    sentence = ''
    for i in txt:
        time.sleep((random.randint(0, 3))/15)
        ClearConsole()
        sentence += i
        print(sentence)

def doNothing():
    pass

class MiniWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('550x130+450+280')
        #Using the doNothing function:
        self.window.protocol('WM_DELETE_WINDOW', doNothing)
        self.window.resizable(False, False)
    def interfaceInput(self, txt):
        #Use this method to receive an input using a GUI
        self.reset()
        self.txt = breakLine(str(txt))
        self.answer = tkinter.Entry(self.window, width=30)
        question = tkinter.Label(self.window, width=20, text=str(self.txt))
        confirm_button = tkinter.Button(self.window, width=20, text="Ok", command=self.captureInput)
        question.pack()
        self.answer.pack()
        self.answer.focus()
        confirm_button.pack()
        self.window.mainloop() 
        return self.final_answer
    def info(self, txt):
        '''Use this method if you want to give some information
        to the user'''
        self.reset()
        time.sleep(0.1)
        self.txt = breakLine(str(txt))
        info = tkinter.Label(self.window, text=self.txt)
        confirm_button = tkinter.Button(self.window, text="Ok.", command=self.window.quit)
        info.pack()
        confirm_button.pack()
        self.window.mainloop()
    #-----------------------------------------------------------
    '''These are methods that the code uses, you can use them,
        but they aren't too useful for you.
    '''
    def captureInput(self):
        self.final_answer = (self.answer).get()
        self.quit()
    def reset(self):
        self.window.destroy()
        self.__init__()
    def quit(self):
        self.window.quit()

if __name__ == '__main__':
    #If the script is executed, do that:
    ClearConsole()
    printClearing(ansii('Black', 'Red', 'This script needs to be imported, not executed!\n-- Press enter to continue -- '))
    key = input('\033[0;{};{}m'.format(selectColor('Red'), selectColor('Red')+10))
    print('\033[m')
    ClearConsole()