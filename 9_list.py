#리스트에서는 인덱스 접근을 -1부터 할 수 있음
list3 = [11, '홍길동', 19, 180.5]
print(list3[1], '님의 키는', list3[-1], 'cm입니다.')

#리스트에서는 [시작인덱스 : 끝인덱스+1] 으로 구간전송 가능, 리스트 교체
list1 = [11, 22, 33, 44, 55]
list1[0:5] = [0, 1, 2, 3, 4]
print(list1)

#주의사항 : 슬라이싱이로는 1:다 대체가 가능함
nums = [11, 22, 33, 44, 55]
nums[1] = [100, 200, 300]
print(nums)

nums = [11, 22, 33, 44, 55]
nums[1:2] = [100, 200, 300]
print(nums)

#얕은 복사 예제 -> nums2를 수정해도 nums1도 같이 수정
print("\n얕은 복사 예제")
nums1 = [11, 22, 33]
nums2 = []

nums2 = nums1

nums2[0] = 0
print(nums1)
print(nums2)

#깊은 복사 예제 -> nums2를  수정해도 nums1은 유지
print("\n깊은 복사 예제")
nums1 = [11, 22, 33]
nums2 = []

nums2 = nums1[:]

nums2[0] = 0
print(nums1)
print(nums2)

#리스트 비교연산 pdf 30페이지 참고
#리스트 연결연산 pdf 32 ~ 33페이지 참고
#리스트 요소추가, 요소삭제 pdf 36~ 41페이지 참고

#리스트에 요소추가 pdf 36페이지
print("\n리스트 요소추가, 요소삭제")
nums1 = [0, 1, 2, 3, 4]

#append는 마지막에 값 추가
nums1.append(5)
#insert는 원하는 위치에 값 추가
nums1.insert(1, 11)
#del은 원하는 위치의 값 삭제
del nums1[1:3]
#remove는 원하는 값 삭제
nums1.remove(5)
#clear은 전체삭제
nums1.clear()

print(nums1)

#리스트 위치반환, 요소개수 세기 (존재하지 않는 요소 검색시 오류 발생)
print("\n리스트 위치반환, 요소개수 세기")
nums = [0, 1, 2, 3, 4, 4, 5]
print(nums.index(4))
print(nums.count(4))
print(2 in nums)
print(6 not in nums)
