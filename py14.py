import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import json

"""
#연습문제 13.1
entry_fahrenheit = None
entry_celsius = None

def exchange_tem1():
    try:
        f = float(entry_fahrenheit.get())
        c = (f - 32) / 1.8
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 화씨 온도를 입력하세요.")

def exchange_tem2():
    try:
        c = float(entry_celsius.get())
        f = (c * 1.8) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 섭씨 온도를 입력하세요.")

def reset_fields():
    entry_fahrenheit.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)

def buildGUI():
    global entry_fahrenheit, entry_celsius

    ttk.Label(win, text='화씨 (°F)').pack()
    entry_fahrenheit = ttk.Entry(win)
    entry_fahrenheit.pack()

    ttk.Label(win, text='섭씨 (°C)').pack()
    entry_celsius = ttk.Entry(win)
    entry_celsius.pack()

    ttk.Button(win, text='화씨 -> 섭씨', command=exchange_tem1).pack(pady=5)
    ttk.Button(win, text='섭씨 -> 화씨', command=exchange_tem2).pack(pady=5)
    ttk.Button(win, text='초기화', command=reset_fields).pack(pady=5)
    ttk.Button(win, text='종료', command=win.destroy).pack(pady=5)

win = tk.Tk()
win.title('온도변환기')
win.geometry('300x250')
buildGUI()
win.mainloop()
"""

"""
#연습문제 13.2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

entry_fahrenheit = None
entry_celsius = None

def exchange_tem1():
    try:
        f = float(entry_fahrenheit.get())
        c = (f - 32) / 1.8
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 화씨 온도를 입력하세요.")

def exchange_tem2():
    try:
        c = float(entry_celsius.get())
        f = (c * 1.8) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 섭씨 온도를 입력하세요.")

def reset_fields():
    entry_fahrenheit.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.insert(0, "0")
    entry_celsius.insert(0, "0")

def buildGUI():
    global entry_fahrenheit, entry_celsius

    # 첫째 줄: 화씨/섭씨 레이블과 입력창
    frame_input = ttk.Frame(win)
    frame_input.grid(row=0, column=0, columnspan=4, pady=5)

    ttk.Label(frame_input, text='화씨').grid(row=0, column=0, padx=5)
    entry_fahrenheit = ttk.Entry(frame_input, width=10)
    entry_fahrenheit.grid(row=0, column=1, padx=5)
    entry_fahrenheit.insert(0, "0")

    ttk.Label(frame_input, text='섭씨').grid(row=0, column=2, padx=5)
    entry_celsius = ttk.Entry(frame_input, width=10)
    entry_celsius.grid(row=0, column=3, padx=5)
    entry_celsius.insert(0, "0")

    # 둘째 줄: 버튼 4개 일렬
    ttk.Button(win, text='화씨->섭씨', command=exchange_tem1)\
        .grid(row=1, column=0, padx=0, pady=0, sticky='ew')
    ttk.Button(win, text='섭씨->화씨', command=exchange_tem2)\
        .grid(row=1, column=1, padx=0, pady=0, sticky='ew')
    ttk.Button(win, text='초기화', command=reset_fields)\
        .grid(row=1, column=2, padx=0, pady=0, sticky='ew')
    ttk.Button(win, text='종료', command=win.destroy)\
        .grid(row=1, column=3, padx=0, pady=0, sticky='ew')

    # 열 균등 분배
    for i in range(4):
        win.grid_columnconfigure(i, weight=1)

win = tk.Tk()
win.title('온도변환기-2단계')
win.geometry('300x70')  # 창 너비 약간 증가
win.resizable(False, False)
buildGUI()
win.mainloop()
"""

#연습문제 13.3
"""
entry_fahrenheit = None
entry_celsius = None

def exchange_tem1():
    try:
        f = float(entry_fahrenheit.get())
        c = (f - 32) / 1.8
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 화씨 온도를 입력하세요.")

def exchange_tem2():
    try:
        c = float(entry_celsius.get())
        f = (c * 1.8) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{f:.2f}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 섭씨 온도를 입력하세요.")

def reset_fields():
    entry_fahrenheit.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.insert(0, "0")
    entry_celsius.insert(0, "0")

def buildGUI():
    global entry_fahrenheit, entry_celsius

    # 입력창 프레임
    frame_input = ttk.Frame(win)
    frame_input.grid(row=0, column=0, padx=10, pady=5)

    ttk.Label(frame_input, text='화씨').grid(row=0, column=0, padx=5)
    entry_fahrenheit = ttk.Entry(frame_input, width=10)
    entry_fahrenheit.grid(row=0, column=1, padx=5)
    entry_fahrenheit.insert(0, "0")

    ttk.Label(frame_input, text='섭씨').grid(row=0, column=2, padx=5)
    entry_celsius = ttk.Entry(frame_input, width=10)
    entry_celsius.grid(row=0, column=3, padx=5)
    entry_celsius.insert(0, "0")

    # 버튼 프레임
    frame_buttons = ttk.Frame(win)
    frame_buttons.grid(row=1, column=0, padx=10, pady=5)

    ttk.Button(frame_buttons, text='화씨->섭씨', command=exchange_tem1)\
        .grid(row=0, column=0, padx=0, sticky='ew')
    ttk.Button(frame_buttons, text='섭씨->화씨', command=exchange_tem2)\
        .grid(row=0, column=1, padx=0, sticky='ew')
    ttk.Button(frame_buttons, text='초기화', command=reset_fields)\
        .grid(row=0, column=2, padx=0, sticky='ew')
    ttk.Button(frame_buttons, text='종료', command=win.destroy)\
        .grid(row=0, column=3, padx=0, sticky='ew')

    for i in range(4):
        frame_buttons.grid_columnconfigure(i, weight=1)

win = tk.Tk()
win.title('온도변환기-2단계')
win.geometry('320x90')
win.resizable(False, False)
buildGUI()
win.mainloop()
"""

"""
#연습문제 13.4
def submit():
    name = entry_name.get()
    grade = grade_var.get()
    hobbies = [hobby for var, hobby in zip(hobby_vars, hobby_list) if var.get() == 1]

    print("이름:", name)
    print("학년:", grade)
    print("취미:")
    for h in hobbies:
        print(h)

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

# 학년 (라디오 버튼)
ttk.Label(win, text="학년:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
grade_var = tk.StringVar(value="1학년")
grades = ["1학년", "2학년", "3학년", "4학년"]
for i, g in enumerate(grades):
    ttk.Radiobutton(win, text=g, variable=grade_var, value=g)\
        .grid(row=1, column=1+i, padx=2, pady=2, sticky='w')

# 취미 (한 줄로 정렬된 체크버튼들)
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
"""


#연습문제 13.5
words = {}

def load_words():
    global words
    if os.path.exists("words.txt"):
        with open("words.txt", "r", encoding="utf-8") as file:
            words = json.load(file)
    else:
        words = {}

def save_words():
    with open("words.txt", "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=2)

def add_word():
    word = entry_word.get().strip()
    meaning = entry_meaning.get().strip()
    if word and meaning:
        words[word] = meaning
        messagebox.showinfo("추가 확인", f"단어 '{word}'를 추가했습니다.")
    else:
        messagebox.showwarning("입력 오류", "단어와 뜻을 모두 입력하세요.")

def search_word():
    word = entry_word.get().strip()
    if word in words:
        entry_meaning.delete(0, tk.END)
        entry_meaning.insert(0, words[word])
    else:
        messagebox.showerror("검색 오류", f"'{word}'란 단어는 없습니다.")

def reset_fields():
    entry_word.delete(0, tk.END)
    entry_meaning.delete(0, tk.END)

def quit_program():
    save_words()
    win.destroy()

# 윈도우 생성
win = tk.Tk()
win.title("단어장")
win.geometry("400x150")
win.resizable(False, False)

# 단어 입력
ttk.Label(win, text="단어:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_word = ttk.Entry(win, width=10)
entry_word.grid(row=0, column=1, padx=5, pady=5, sticky='w')
ttk.Button(win, text="검색", command=search_word).grid(row=0, column=2, padx=5)
ttk.Button(win, text="추가", command=add_word).grid(row=0, column=3, padx=5)

# 뜻 입력
ttk.Label(win, text="뜻:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_meaning = ttk.Entry(win, width=40)
entry_meaning.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky='w')

# 초기화 및 종료 버튼
ttk.Button(win, text="초기화", command=reset_fields).grid(row=2, column=1, padx=5, pady=10, sticky='e')
ttk.Button(win, text="종료", command=quit_program).grid(row=2, column=2, padx=5, pady=10, sticky='w')

# 프로그램 시작 시 단어장 불러오기
load_words()
win.mainloop()
