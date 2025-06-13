import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

#루트 윈도우 만들기
"""
import tkinter as tk

root_win = tk.Tk()
root_win.title('나의 첫 윈도우')
root_win.geometry('500x200-0+50')   #너비, 높이, 가로위치, 세로위치
root_win.resizable(width=True, height=False)   #고정 활성화/비활성화 -> 마우스로 창 크기 바꾸기

root_win.mainloop()
"""

#ttk 위젯 -> 기본 명령문 출력
"""
def display_options(widget):
    config = widget.configure()
    for key, value in config.items():
        print(f'{key:15s}\t{value}')

widget = ttk.Label(None)
display_options(widget)
"""

#label 위젯, 텍스트 출력
"""
def buildGUI():
    text_label1 = ttk.Label(win, text='안녕하세요')

    text_label2 = ttk.Label(win)
    text_label2.configure(text = '반가워요',
                          foreground = 'white',
                          background='red',
                          font=('맑은 고딕', 20)
    )
    
    text_label1.pack()
    text_label2.pack()

win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
"""

#버튼 위젯, 이름 입력후 출력
"""
def buildGUI():
    global text_label
    text_label = ttk.Label(win, text ='안녕하세요')

    global name
    name = tk.StringVar()
    input_entry = ttk.Entry(win, textvariable = name)

    input_btn = ttk.Button(win, text='입력',
                           command = input_btn_handler)
    quit_btn = ttk.Button(win, text='종료',
                           command = win.destroy)

    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text='반가워요, ' + name.get())
    name.set('')

win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
"""

#텍스트 위젯, 스크롤위젯, 입력후 출력
"""
def buildGUI():
    global text_area
    text_area = scrolledtext.ScrolledText(win, width=30, height=5, wrap=tk.WORD)

    input_btn = ttk.Button(win, text='출력',
                           command = input_btn_handler)


    text_area.pack()
    input_btn.pack()

def input_btn_handler():
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0, tk.END)

win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
"""

#체크버튼 위젯
"""
def buildGUI():
    global check
    check = tk.IntVar()
    check_btn = ttk.Checkbutton(win, text='옵션을 선택하세요',
                                variable=check,
                                command=open_dialog_box)
    
    check_btn.pack()

def open_dialog_box():
    if check.get() == 1:
        messagebox.showinfo('확인', '옵션 선택')
    else:
        messagebox.showinfo('확인', '옵션 해제')
        

win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
"""

#라디오버튼 위젯
"""
GENDERS = ['남성', '여성', '기타']
COLORS = ['red', 'yellow', 'purple']

def buildGUI():
    global check
    text_label = ttk.Label(win, text='당신의 성별은? ')
    text_label.pack()

    global gender
    gender = tk.IntVar()
    for i in range(3):
        radio_btn = ttk.Radiobutton(win,
                                    text=GENDERS[i],
                                    value=i,
                                    variable=gender,
                                    command=radio_btn_handler
        )
        radio_btn.pack()

    gender.set(-1)

def radio_btn_handler():
    choice = gender.get()
    win.configure(background=COLORS[choice])
        

win = tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
"""



#위젯배치 -> pack() -> 위젯을 블럭으로 구성, pdf 56, 57페이지 여백 참고
"""
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.pack()
    btn2.pack(ipadx=10, ipady=10)
    btn3.pack(padx=10, pady=10)
    btn4.pack(fill=tk.X)
    btn5.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('300x200')
buildGUI()
win.mainloop()
"""

#위젯배치 -> grid() -> 위젯을 절대 위치에 부착 (매트릭스 행렬)
#그냥 PDF 보고 하기
"""
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=1, column=1)
    btn4.grid(row=1, column=2)
    btn5.grid(row=2, column=2)


win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('300x200')
buildGUI()
win.mainloop()
"""

#위젯배치 -> frame()
"""
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='매우 긴 너비와 높이를 갖는\n버\n튼\n2')
    btn_group = ttk.Frame(win)
    btn3 = ttk.Button(btn_group, text='버튼3')
    btn4 = ttk.Button(btn_group, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.grid(row=0, column=0, sticky='se')
    btn2.grid(row=0, column=1)
    btn3.pack(side=tk.LEFT)
    btn4.pack(side=tk.LEFT)
    btn_group.grid(row=1, column=1, sticky='w')
    btn5.grid(row=2, column=0)


win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('300x200')
buildGUI()
win.mainloop()
"""

#객체지향적으로 구성된 GUI
class SayHelloWin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('버튼 위젯 예-OOP')
        self.__buildGUI()

    def __buildGUI(self):
        self.text_label = ttk.Label(self.win, text='안녕하세요')
        self.name = tk.StringVar()
        input_entry = ttk.Entry(self.win, textvariable=self.name)
        input_btn = ttk.Button(self.win, text = '입력', command=self.__input_btn_handler)
        quit_btn = ttk.Button(self.win, text='종료', command=self.win.destroy)

        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        quit_btn.pack()

    def __input_btn_handler(self):
        self.text_label.configure(text='반가워요, ' + self.name.get())
        self.name.set('')

hello = SayHelloWin()
hello.win.mainloop()
