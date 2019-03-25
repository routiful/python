def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
num = 0
while num < len(sample_temperature_list):
    sample_temperature_list[num] = fahrenheit_to_celsius(sample_temperature_list[num])
    sample_temperature_list[num] = round(sample_temperature_list[num], 2)
    num += 1
    
# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))