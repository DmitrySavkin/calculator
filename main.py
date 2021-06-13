from functools import partial
from tkinter import *
from Parser import Parser
import shelve
from tkinter.messagebox import showerror
# globally declare the expression variable
class Calculator:

    def __init__(self):
        self.expression = ""
        self.window = Tk()
        self.parser = Parser()
        self.window.title("Calculator")
        self.equation = StringVar()
        self.entry = Entry(self.window, textvariable=self.equation)
        self.entry.grid(row=1)
        buttonFrame = Frame(self.window)
        buttonFrame.grid(row=3)
        for i in range(9):
            Button(buttonFrame, command=partial(self.press, i + 1), text=str(i + 1), height=4, width=4) \
                .grid(row=i // 3, column=i % 3)

        btnEquals = Button(buttonFrame, text='=', command=lambda: self.result(), height=4, width=4) \
            .grid(row=4, column=0)
        btnZero = Button(buttonFrame, command=partial(self.press, 0), text=str(0), height=4, width=4) \
            .grid(row=4, column=1)
        btnClean = Button(buttonFrame, command=lambda :self.clean(), text='C', height=4, width=4) \
            .grid(row=4, column=2)
        btnLeftBracket = Button(buttonFrame, command=partial(self.press, ')'), text=')', height=4, width=4) \
            .grid(row=0, column=4)
        btnRightBracket = Button(buttonFrame, command=partial(self.press, '('), text='(', height=4, width=4) \
            .grid(row=1, column=4)
        btnPlus = Button(buttonFrame, command=partial(self.press, '+'), text='+', height=4, width=4) \
            .grid(row=0, column=5)
        btnMinus = Button(buttonFrame, command=partial(self.press, '-'), text='-', height=4, width=4) \
            .grid(row=1, column=5)
        # btnProd = Button(buttonFrame, command=partial(self.press, '*'), text='*', height=4, width=4) .grid(row=2, column=5)
        self.window.mainloop()


    def clean(self):
        self.expression = ""
        self.equation.set(self.expression)
    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)


    def result(self):
        print("Result")
        result = self.parser.parse(self.expression)
        self.equation.set(result)


def makeWidget():

    global equation


if __name__ == '__main__':
    c = Calculator()
