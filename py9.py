#9.1, 9.2 연습문제 (소수점, 리스트)
scores = []

for i in range(3):
    x = int(input(f"#{i+1}?"))
    scores.append(x)

print("\n[점수 출력]")
print("입력 점수:", end='')
sum = 0
for i in range(3):
    print(scores[i], end = ' ')
    sum = sum + scores[i]
print(f"\n평균: {sum/3:0.1f}")

print("\n[검색]")
a = int(input("찾고자 하는 점수는?"))
c = scores.index(88)
print(f"{a}점은 {c+1}번 학생의 점수입니다.")

#9.3 연습문제
shopping_bag = []
print("[구입]")
while True:
    item = str(input("상품명?"))
    if (item == ''):
        break
    shopping_bag.append(item)
    print(f"장바구니에 {item}가(이) 담겼습니다.\n")

print(f"\n>>> 장바구니 보기: {shopping_bag}")


#9.4 연습문제
shopping_bag = {}
print("[구입]")
while True:
    item = str(input("상품명?"))
    if (item == ''):
        break
    s = int(input("수량은?"))
    shopping_bag[item] = s
    print(f"장바구니에 {item} {s}개가 담겼습니다.\n")

print(f"\n>>> 장바구니 보기: {shopping_bag}")

print("[검색]")
x = str(input("장바구니에서 확인하고자 하는 상품은?"))

if x in shopping_bag:
    print(f"{x}은(는) {shopping_bag[x]}개 담겨 있습니다.")
else:
    print("존재하지 않습니다.")

