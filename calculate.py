 # calc.py - a Python calculator
from tkinter import *


class Calculator(Frame):
    def __init__(self):
        self.total = 0
        self.current = '0'
        self.store = ''
        self.new_num = True
        self.combo = False
        self.op = ''

    def num_press(self, num):

        #if operation in stack, clear output field for new number
        if self.combo:
            origin = text_box.get()
        elif self.op:
            self.combo = True
            text_box.delete(0,END)
        #if no op in stack keep the old number to add up with new one
        else:
            origin = text_box.get()

        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in origin:
                    return
            self.current = origin + temp2
        self.display(self.current)

    def oper(self,op):
        if self.combo:
            self.execute()
            self.op = op
            self.combo = False
        self.store = text_box.get()
        self.op = op
        self.new_num = True

    def execute(self):
        if self.op == '+':
            self.current = float(self.store) + float(self.current)
        elif self.op == '-':
            self.current = float(self.store) - float(self.current)
        elif self.op == '*':
            self.current = float(self.store) * float(self.current)
        elif self.op == '/':
            self.current = float(self.store) / float(self.current)

        self.op = ''
        self.display(self.current)

    def final(self):
        if self.op:
            self.execute()
            self.new_num = True
        else:
            return

    def display(self, number):
        text_box.delete(0, END)
        text_box.insert(0, number)

    def clear(self):
        self.display(0)
        self.current = '0'
        self.new_num = True

    def all_clear(self):
        self.display(0)
        self.op = ''
        self.store = ''
        self.current = ''
        self.new_num = True
        self.combo = False

sum1 = Calculator()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = 5)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.oper("/")
bttn_div.grid(row = 1, column = 3, pady = 5)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.oper("*")
bttn_mult.grid(row = 2, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.oper("-")
minus.grid(row = 3, column = 3, pady = 5)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = 5)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.oper('+')
add.grid(row = 4, column = 3, pady = 5)

clear = Button(calc, text = "C")
clear["command"] = sum1.clear
clear.grid(row = 5, column = 1, pady = 5)

all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 5, column = 2, pady = 5)

equals = Button(calc, text = "=")
equals["command"] = sum1.final
equals.grid(row = 5, column = 3, pady = 5)

root.mainloop()
