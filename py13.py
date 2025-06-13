import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

#연습문제 13.1
def buildGUI():
    global text_label1
    text_label1 = ttk.Label(win, text='화씨')

    global temp1
    temp1 = tk.IntVar()
    input_entry = ttk.Entry(win, textvariable = temp1)

    global text_label2
    text_label2 = ttk.Label(win, text='섭씨')

    global temp2
    temp2 = tk.IntVar()
    input_entry = ttk.Entry(win, textvariable = temp2)
    
    btn1 = ttk.Button(win, text='화씨->섭씨')
    btn2 = ttk.Button(win, text='섭씨->화씨')
    btn3 = ttk.Button(win, text='초기화')
    btn4 = ttk.Button(win, text='종료')

def input_btn_handler():
    text_label.configure(text='반가워요, ' + name.get())
    name.set('')
    
    text_label1.pack()
    input_entry.pack()
    text_label2.pack()
    input_entry.pack()
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()


 
win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('300x200')
buildGUI()
win.mainloop()
