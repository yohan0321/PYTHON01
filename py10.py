#연습문제 10.2
"""
x = []

def find_max(x):
    max = 0
    for i in range(len(x)):
        if max < x[i]:
            max = x[i]

    return max

for i in range(0, 5):
    a = int(input("정수 입력: "))
    x.append(a)

print(x)
max = find_max(x)
print(f"가장 큰 정수는 {max}입니다.")
"""

#연습문제 10.3, 10.4
"""
def input_scores(scores):
    i = 0
    while True:
        x = int(input(f"#{i+1}?"))
        if (x < 0):
            return scores
        scores.append(x)
        i = i + 1

def show_scores(scores):
    print("\n[점수 출력]")
    print("개인 점수:", end='')
    for i in range(len(scores)):
        print(scores[i], end = ' ')

def get_average(scores):
    sum = 0
    for i in range(len(scores)):
        sum = sum + scores[i]
    sum = sum / len(scores)
    return sum

def search(scores, n):
    if n in scores:
        print(f"{n}점은 {scores.index(n)+1}번 학생의 점수입니다.")
    else:
        print(f"{n}점을 받은 학생은 없습니다.")

scores = []
scores = input_scores(scores)
show_scores(scores)
avr = get_average(scores)
print(f"\n평균: {avr:.1f}")
print("[검색]")
n = int(input("찾고자 하는 점수는?"))
search(scores, n)
"""

#연습문제 10.6
def buy(shopping_bag):
    print("[구입]")
    item = str(input("상품명?"))
    if (item == ''):
        return False
    s = int(input("수량은?"))
    shopping_bag[item] = s
    print(f"장바구니에 {item} {s}개가 담겼습니다.\n")

def show(shopping_bag):
    print(f"\n>>> 장바구니 보기: {shopping_bag}")

def find(shopping_bag):
    print("\n[검색]")
    x = str(input("장바구니에서 확인하고자 하는 상품은?"))

    if x in shopping_bag:
        print(f"{x}은(는) {shopping_bag[x]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {x}은(는) 없습니다.")

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)








    
