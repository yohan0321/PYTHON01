#연습문제 12.1
"""
lines = []
i = 0

with open('readme.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines.append(line.strip('\n'))
        print(f"{i+1}:{lines[i]}")
        i = i + 1
"""

#연습문제 12.3
"""
filepath = 'shoppingbag.txt'
shopping_bag = []

def load_data():
    try:
        with open('shoppingbag.txt', 'r', encoding='utf-8') as file:
            for line in file:
                shopping_bag.append(line.strip())
            print("[파일 읽기]")
            print(f">>> 장바구니 보기: {shopping_bag}")
    except FileNotFoundError:
        pass
        
def save_data():
    while True:
        print("[구입]")
        a = str(input("상품명?"))
        if (a == ''):
            break
        shopping_bag.append(a)
        print(f"장바구니에 {a}가(이) 담겼습니다.")

def save_file():
    with open('shoppingbag.txt', 'w', encoding='utf-8') as file:
        for i in shopping_bag:
            file.write(i + '\n')
    print(f">>> 장바구니 보기: {shopping_bag}")
        
            


load_data()
save_data()
save_file()
"""


#연습문제 12.4
"""
import pickle
from datetime import datetime

class Time:
    def __init__(self, h, m):
        self.hour = h
        self.minute = m

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

def get_current_time():
    now = datetime.now()
    return Time(now.hour, now.minute)

def save_time(t):
    with open('last.dat', 'wb') as file:
        pickle.dump(t, file)

def load_time():
    try:
        with open('last.dat', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def main():
    last_time = load_time()

    if last_time is None:
        print("안녕하세요, 처음 실행되었습니다.")
    else:
        print(f"안녕하세요, 마지막으로 {last_time}에 실행되었습니다.")

    current_time = get_current_time()
    print(f"지금은 {current_time} 입니다.")
    save_time(current_time)

if __name__ == '__main__':
    main()
"""



#연습문제 12.2
import pickle
import os

filefath = 'score.bin'
filename = 'score.bin'

def load_data():
    try:
        print("[파일 읽기]\n")
        with open('score.bin', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        pass

def show_scores(scores):
    print("\n[점수 출력]")
    print("개인 점수:", end='')
    for i in range(len(scores)):
        print(scores[i], end = ' ')
        
def input_scores():
    scores = []
    i = 0
    while True:
        x = int(input(f"#{i+1}?"))
        if (x < 0):
            return scores
            break
        scores.append(x)
        i = i + 1

def save_data(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)
        
def get_average(scores):
    sum = 0
    for i in range(len(scores)):
        sum = sum + scores[i]
    sum = sum / len(scores)
    return sum

if os.path.exists(filename):
    scores = load_data()
    show_scores(scores)
    avr = get_average(scores)
    print(f"\n평균: {avr:.1f}")
else:
    print("[점수 입력]")
    scores = input_scores()
    save_data(scores)
    show_scores(scores)
    avr = get_average(scores)
    print(f"\n평균: {avr:.1f}")








