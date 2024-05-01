# Task 2

import tkinter as tk

root = tk.Tk()

def get_input():
    user_input_f = entery_f.get()
    a = eval(user_input_f)

    user_input_s = entery_s.get()
    b = eval(user_input_s)

    user_input_si = entery_si.get()
    si = str(user_input_si)

    if si == "+":
        print(a+b)
    elif si == "*":
        print(a*b)
    elif si == "-":
        print(a-b)
    elif si == "/":
        print(a/b)
    elif si == "^":
        print(a**b)
    else:
        print("Your input is invalid")


#first number
label = tk.Label(root,text="Type your first value here: ")
label.pack()
entery_f = tk.StringVar()
entry = tk.Entry(root,textvariable=entery_f)
entry.pack()

#seconde number
label = tk.Label(root,text="Type your second value here: ")
label.pack()
entery_s = tk.StringVar()
entry = tk.Entry(root,textvariable=entery_s)
entry.pack()

#sign
label = tk.Label(root,text="Type your sign value here: ")
label.pack()
entery_si = tk.StringVar()
entry = tk.Entry(root,textvariable=entery_si)
entry.pack()

label = tk.Label(root,text="")
label.pack()

#calculate button
button = tk.Button(root,text="Get input",command=get_input)
button.pack()


root.mainloop()
