# 자리수 합 리턴
def sum_digit(num):
    digit = 0
    while True:
        if num == 0:
        	return digit
        
        digit += num % 10
        num = int(num / 10)
		

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
result = 0
for num in range(1, 1001):
    result += sum_digit(num)
    
print(result)