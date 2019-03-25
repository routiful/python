# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
num = 1
while num <= 10:
    numbers.append(num)
    num += 1

print(numbers)

# numbers에서 홀수 제거
num = 0
while num < len(numbers):
    if numbers[num] % 2 == 1:
        del numbers[num]
    num += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)