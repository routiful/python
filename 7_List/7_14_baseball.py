#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from random import randint

selected_num = []

attempt = 0
strike = 0
ball = 0

i = 0
while i < 3:
    get_num = randint(0, 9)
    if (get_num not in selected_num):
        selected_num.append(get_num)
        i += 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

while strike < 3:
    strike = 0
    ball = 0
    input_num = []
    print("\n세 수를 하나씩 차례대로 입력하세요.")

    i = 1
    while i <= 3:
        get_num = int(input("{}번째 수를 입력하세요: ".format(i)))
        if (get_num in input_num) :
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        if (get_num > 9) or (get_num < 0):
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        input_num.append(get_num)
        i += 1

    i = 0
    while i < 3:
        if (input_num[i] == selected_num[i]):
            strike += 1
        elif (input_num[i] in selected_num):
            ball += 1
        i += 1

    print(selected_num)
    print(input_num)
    print("{}S {}B".format(strike, ball))
    
	attempt += 1

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(attempt))

    
