# APP MADE BY UZIEL
# I TRY TO MAKE IT AS SIMPLE AS POSSIBLE SO IT HAS A LOT OF BUGS, FEEL FRE TO USE THIS CODE
# INSTAGRAM: uziel_acuna_25 
# TWITTER: @UzielAcuna25

from tkinter import Tk, Label, Button, StringVar, Entry, Frame
from functions import number, add, sub, mult, div, result, errase, re

# WINDOW
wind = Tk()
wind.resizable(False, False)

# FRAME
frame = Frame(wind)
frame.config(background='#363630')
frame.pack()

# LABEL
data_LS = StringVar()
data_L = Label(frame, textvariable=data_LS)
data_L.config(background='#363630', fg='#E0C500', justify='left')
data_L.grid(row=0, column=0, columnspan=4, sticky='e')

# ENTRY
data_T = StringVar()
data = Entry(frame, textvariable=data_T)
data.config(background='black', fg='#E0C500', justify='right')
data.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

# BUTTONS
buttonC = Button(frame, text='C', width=3, command=lambda:errase(data_T, data_LS))
buttonC.grid(row=2, column=0)
buttonDiv = Button(frame, text='/', width=3, command=lambda:div(data_T))
buttonDiv.grid(row=2, column=1)
buttonMult = Button(frame, text='X', width=3, command=lambda:mult(data_T))
buttonMult.grid(row=2, column=2)
buttonR = Button(frame, text='<<', width=3, command=lambda:re(data_T, data_LS))
buttonR.grid(row=2, column=3)

button7 = Button(frame, text='7', width=3, command=lambda:number('7', data_T, data_LS, data_L))
button7.grid(row=3, column=0)
button8 = Button(frame, text='8', width=3, command=lambda:number('8', data_T, data_LS, data_L))
button8.grid(row=3, column=1)
button9 = Button(frame, text='9', width=3, command=lambda:number('9', data_T, data_LS, data_L))
button9.grid(row=3, column=2)
buttonSub = Button(frame, text='-', width=3, command=lambda:sub(data_T))
buttonSub.grid(row=3, column=3)

button4 = Button(frame, text='4', width=3, command=lambda:number('4', data_T, data_LS, data_L))
button4.grid(row=4, column=0)
button5 = Button(frame, text='5', width=3, command=lambda:number('5', data_T, data_LS, data_L))
button5.grid(row=4, column=1)
button6 = Button(frame, text='6', width=3, command=lambda:number('6', data_T, data_LS, data_L))
button6.grid(row=4, column=2)
buttonSum = Button(frame, text='+', width=3, command=lambda:add(data_T))
buttonSum.grid(row=4, column=3)

button1 = Button(frame, text='1', width=3, command=lambda:number('1', data_T, data_LS, data_L))
button1.grid(row=5, column=0)
button2 = Button(frame, text='2', width=3, command=lambda:number('2', data_T, data_LS, data_L))
button2.grid(row=5, column=1)
button3 = Button(frame, text='3', width=3, command=lambda:number('3', data_T, data_LS, data_L))
button3.grid(row=5, column=2)
buttonEqual = Button(frame, text='=', width=3, height=3, command=lambda:result(data_T, data_LS))
buttonEqual.grid(row=5, column=3, rowspan=2)

button0 = Button(frame, text='0', width=8, command=lambda:number('0', data_T, data_LS, data_L))
button0.grid(row=6, column=0, columnspan=2)
buttonDot = Button(frame, text='.', width=3, command=lambda:number('.', data_T, data_LS, data_L))
buttonDot.grid(row=6, column=2)

# WINDOW LOOP
if __name__ == '__main__':
    wind.mainloop()