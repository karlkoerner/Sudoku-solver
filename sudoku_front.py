from sudoku_solve import main, GRID
from tkinter import *
from tkinter import messagebox
from time import sleep

root = Tk()
root.title("SUDOKU")
frame0 = LabelFrame(root, padx=5, pady=5)
frame0.pack(padx=100, pady=10)

frameA1 = LabelFrame(frame0, padx=5, pady=5)
frameA2 = LabelFrame(frame0, padx=5, pady=5)
frameA3 = LabelFrame(frame0, padx=5, pady=5)

frameB1 = LabelFrame(frame0, padx=5, pady=5)
frameB2 = LabelFrame(frame0, padx=5, pady=5)
frameB3 = LabelFrame(frame0, padx=5, pady=5)

frameC1 = LabelFrame(frame0, padx=5, pady=5)
frameC2 = LabelFrame(frame0, padx=5, pady=5)
frameC3 = LabelFrame(frame0, padx=5, pady=5)

frameA1.grid(row=0, column=0)
frameA2.grid(row=0, column=1)
frameA3.grid(row=0, column=2)

frameB1.grid(row=1, column=0)
frameB2.grid(row=1, column=1)
frameB3.grid(row=1, column=2)

frameC1.grid(row=2, column=0)
frameC2.grid(row=2, column=1)
frameC3.grid(row=2, column=2)

frames = [frameA1, frameA2, frameA3, frameB1, frameB2, frameB3, frameC1, frameC2, frameC3]
framesa = [frameA1, frameA2, frameA3]
framesb = [frameB1, frameB2, frameB3]
framesc = [frameC1, frameC2, frameC3]

liste = []

def add_boxes(frames):
    global liste
    for frame in frames:
        TA1 = Text(frame, height=1, width=2)
        TA2 = Text(frame, height=1, width=2)
        TA3 = Text(frame, height=1, width=2)

        TA1.grid(row=0, column=0)
        TA2.grid(row=0, column=1)
        TA3.grid(row=0, column=2)

        liste.extend((TA1, TA2, TA3))

    for frame in frames:
        TB1 = Text(frame, height=1, width=2)
        TB2 = Text(frame, height=1, width=2)
        TB3 = Text(frame, height=1, width=2)

        TB1.grid(row=1, column=0)
        TB2.grid(row=1, column=1)
        TB3.grid(row=1, column=2)

        liste.extend((TB1, TB2, TB3))

    for frame in frames:
        TC1 = Text(frame, height=1, width=2)
        TC2 = Text(frame, height=1, width=2)
        TC3 = Text(frame, height=1, width=2)

        TC1.grid(row=2, column=0)
        TC2.grid(row=2, column=1)
        TC3.grid(row=2, column=2)

        liste.extend((TC1, TC2, TC3))

add_boxes(framesa)
add_boxes(framesb)
add_boxes(framesc)


def get_errors(input):
    try:
        input = int(input)
    except ValueError:
        messagebox.showerror("Error", "Nur ZAHLEN von 0-9!!!")
        return None
    if input < 0 or input > 9:
        messagebox.showerror("Error", "Nur Zahlen von 0-9!!!")
        return None
    else:
        return input

def get_input():
    index1 = 0
    index2 = 0
    for text in liste:
        input = text.get("1.0","end-1c")
        if input == "":
            input = 0
        input = get_errors(input)
        GRID[index1][index2] = int(input)
        index2 += 1
        if index2 == 9:
            index2 = 0
            index1 += 1
        if index1 == 9:
            index1 = 0
    print(GRID)

def print_solution():
    for text in liste:
        text.delete(1.0, END)
    index = 0
    for row in GRID:
        for num in row:
            liste[index].insert(END, str(num))
            index += 1

def start():
    get_input()
    main()
    Label(root, text="Fertig!!!").pack()
    print_solution()


start = Button(root, text="START", command=start).pack()


root.mainloop()
