#딕셔너리 생성
d = {'python':'파이썬', 'basic':'기초', 'programming':'프로그래밍'}
print(d)

print(d['python'])
#get() = 요소에 접근하기
print(d.get('python'))

key = 0
if key in d:
    print(d[key])



#딕셔너리 요소추가, 요소삭제
d['x'] = '엑스'
print(d)

del d['x']
print(d)

d.clear()
print(d)
