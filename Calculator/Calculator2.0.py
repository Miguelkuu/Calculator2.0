from tkinter import *


root = Tk()
root.title("Calculator 2.0")
root.geometry("208x277")
root.resizable(False, False)



class Calculator:
    def __init__(self):
        self.buttons()
        self.labels()
        self.numbers = []
        self.ope = []
        self.total = []
        self.num1 = ""
        self.ope_total = self.ope.count()

    
    def labels(self):
        self.display_one = Label(root, text=" ", justify="right", height=2, bg="grey", fg="white")
        self.display_one.grid(column=0, row=1, columnspan=4, sticky="we")

        self.display_two = Label(root, height=2, bg="grey", fg="white")
        self.display_two.grid(column=0, row=0, columnspan=4, sticky="we")


    def buttons(self):
        self.zero_button = Button(root, text="0", height=2, width=6, bg="grey", fg="white")
        self.zero_button.grid(column=0, row=6, columnspan=2, sticky="we")
        self.zero_button["command"] = lambda: self.add_x_to_num("0")

        self.dot_button = Button(root, text=".", height=2, width=6, bg="grey", fg="white")
        self.dot_button.grid(column=2, row=6)
        self.dot_button["command"] = lambda: self.add_x_to_num(".")

        self.equal_button = Button(root, text="=", height=2, width=6, bg="light grey", fg="black")
        self.equal_button.grid(column=3, row=6)

        self.one_button = Button(root, text="1", height=2, width=6, bg="grey", fg="white")
        self.one_button.grid(row=5, column=0)
        self.one_button["command"] = lambda: self.add_x_to_num("1")

        self.two_button = Button(root, text="2", height=2, width=6, bg="grey", fg="white")
        self.two_button.grid(row=5,column=1)
        self.two_button["command"] = lambda: self.add_x_to_num("2")

        self.three_button = Button(root, text="3", height=2, width=6, bg="grey", fg="white")
        self.three_button.grid(row=5, column=2)
        self.three_button["command"] = lambda: self.add_x_to_num("3")

        self.plus_button = Button(root, text="+", height=2,width=6, bg="light grey", fg="black")
        self.plus_button.grid(row=5, column=3)
        self.plus_button["command"] = lambda: self.add_y_to_ope("+")

        self.four_button = Button(root, text="4", height=2, width=6, bg="grey", fg="white")
        self.four_button.grid(row=4, column=0)
        self.four_button["command"] = lambda: self.add_x_to_num("4")

        self.five_button = Button(root, text="5", height=2, width=6, bg="grey", fg="white")
        self.five_button.grid(row=4, column=1)
        self.five_button["command"] = lambda: self.add_x_to_num("5")

        self.six_button = Button(root, text="6", height=2, width=6, bg="grey", fg="white")
        self.six_button.grid(row=4, column=2)
        self.six_button["command"] = lambda: self.add_x_to_num("6")

        self.minus_button = Button(root, text="-", height=2, width=6, bg="light grey", fg="black")
        self.minus_button.grid(row=4, column=3)
        self.minus_button["command"] = lambda: self.add_y_to_ope("-")

        self.seven_button = Button(root, text="7", height=2, width=6, bg="grey", fg="white")
        self.seven_button.grid(row=3, column=0)
        self.six_button["command"] = lambda: self.add_x_to_num("7")

        self.eigth_button = Button(root, text="8", height=2, width=6, bg="grey", fg="white")
        self.eigth_button.grid(row=3, column=1)
        self.six_button["command"] = lambda: self.add_x_to_num("8")

        self.nine_button = Button(root, text="9", height=2, width=6, bg="grey", fg="white")
        self.nine_button.grid(row=3, column=2)
        self.six_button["command"] = lambda: self.add_x_to_num("9")

        self.multiply_button = Button(root, text="*", height=2, width=6, bg="light grey", fg="black")
        self.multiply_button.grid(row=3, column=3)
        self.multiply_button["command"] = lambda: self.add_y_to_ope("*")

        self.clear_button = Button(root, text="AC",height=2, width=6, bg="light grey", fg="black")
        self.clear_button.grid(column=0, row=2, columnspan=2, sticky="we")
        self.clear_button["command"] = self.clear_all

        self.negative_button = Button(root, text="-/+", height=2, width=6, bg="light grey", fg="black")
        self.negative_button.grid(column=2, row=2)

        self.divide_button = Button(root, text="/", height=2, width=6, bg="light grey", fg="black")
        self.divide_button.grid(column=3, row=2)
        self.divide_button["command"] = lambda: self.add_y_to_ope("/")

    def add_x_to_num(self, x):
        if x == "-":
            if "-" in self.num1:
                self.num1 = self.num1.lstrip("-")
                return
            self.num1 = x + self.num1
            return
        elif "." in self.num1:
            return
        self.num1 = self.num1 + x

    def add_y_to_ope(self, y):
        if self.ope_total > 0:
            self.num1 = int(self.num1)
            self.numbers.append(self.num1)
            if y == "+":
               self.ope.append("+")
            elif y == "-":
               self.ope.append("-")
            elif y == "*":
               self.ope.append("*")
            elif y == "/":
               self.ope.append("/")
        elif y == "+":
            self.ope.append("+")
        elif y == "-":
            self.ope.append("-")
        elif y == "*":
            self.ope.append("*")
        elif y == "/":
            self.ope.append("/")
        self.num1 = int(self.num1)
        self.numbers.append(self.num1)
        self.num1 = ""
        print(self.num1)
        print(self.numbers)

    def clear_all(self):
        self.numbers = []
        self.ope = []
        self.total = []
        self.num1 = ""
 
        
Calculator()
root.mainloop()