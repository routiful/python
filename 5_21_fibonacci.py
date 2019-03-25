first_num = 1
second_num = 1

i = 2
print(first_num)
print(second_num)
while i < 20:
    num = second_num
    second_num = first_num + second_num
    first_num = num
    
    print(second_num)
    
    i += 1