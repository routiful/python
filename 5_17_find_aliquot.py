num = 120
sub = 1
count = 0
while sub <= num:
    if num % sub == 0:
        print(sub)
        count = count + 1
    sub = sub + 1
    
print("{}의 약수는 총 {}개입니다.".format(num, count))