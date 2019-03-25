numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for index in range(int(len(numbers) / 2)):
    left = numbers[index]
    right = numbers[len(numbers) - index - 1]
    
    temp = left
    left = right
    right = temp
    
    numbers[index] = left
    numbers[len(numbers) - index - 1] = right

print("뒤집어진 리스트: " + str(numbers))