import tkinter as tk
from tkinter import ttk

def submit():
    name = entry_name.get()
    grade = grade_var.get()
    hobbies = [hobby for var, hobby in zip(hobby_vars, hobby_list) if var.get() == 1]

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(f"이름: {name}\n")
        file.write(f"학년: {grade}\n")
        file.write("취미:\n")
        for h in hobbies:
            file.write(f"{h}\n")

def quit_program():
    win.destroy()

win = tk.Tk()
win.title("회원 가입")
win.geometry("400x180")
win.resizable(False, False)

# 이름
ttk.Label(win, text="이름:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_name = ttk.Entry(win, width=30)
entry_name.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky='w')

# 학년
ttk.Label(win, text="학년:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
grade_var = tk.StringVar(value="1학년")
grades = ["1학년", "2학년", "3학년", "4학년"]
for i, g in enumerate(grades):
    ttk.Radiobutton(win, text=g, variable=grade_var, value=g)\
        .grid(row=1, column=1+i, padx=2, pady=2, sticky='w')

# 취미
ttk.Label(win, text="취미:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
hobby_list = ["영화시청", "음악감상", "사진찍기", "운동"]
hobby_vars = [tk.IntVar() for _ in hobby_list]
for i, hobby in enumerate(hobby_list):
    ttk.Checkbutton(win, text=hobby, variable=hobby_vars[i])\
        .grid(row=2, column=1 + i, padx=2, pady=2, sticky='w')

# 버튼
ttk.Button(win, text="입력", command=submit).grid(row=3, column=2, padx=5, pady=10)
ttk.Button(win, text="종료", command=quit_program).grid(row=3, column=3, padx=5, pady=10)

win.mainloop()
