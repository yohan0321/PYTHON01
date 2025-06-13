#파일 열기
import os

filename = 'example.txt'
if os.path.exists(filename):
    file = open(filename, 'w')
    file.close()
    print('파일 열고 닫기 완료')
else:
    print(f"error: {filename}이 존재하지 않습니다.")

#파일 쓰기
num = 2
name = '홍길동'

with open('example.txt', 'w') as file:
    file.write("1 이찬수\n")
    file.write(f"{num} {name}")

#파일 텍스트 출력
with open('example.txt', 'r') as file:
    all1 = file.read()
    all2 = file.readlines()

print(all1)
print(all2)


#파일을 한줄 씩 읽기
lines = []
with open('example.txt', 'r') as file:
    while True:
        line = file.readline()

        if line == '':
            break

        lines.append(line.strip())

print(lines)


#이진 파일 입출력 1
import pickle

filepath = 'example.bin'

def save_data(num, name, height, scores):
    with open(filepath, 'wb') as file:
        pickle.dump(num, file)
        pickle.dump(name, file)
        pickle.dump(height, file)
        pickle.dump(scores, file)

def load_data():
    with open(filepath, 'rb') as file:
        num = pickle.load(file)
        name = pickle.load(file)
        height = pickle.load(file)
        scores = pickle.load(file)

    return num, name, height, scores


num, name, height = 123, '홍길동', 180.5
scores = {'mid':90, 'fin':95, 'rep':10, 'att':10}

save_data(num, name, height, scores)

r_num, r_name, r_height, r_scores = load_data()

print(r_num)
print(r_name)
print(r_height)
print(r_scores)
