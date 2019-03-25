#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from random import randint

answer = randint(1,20)
count = 0
OPPORTUNITY = 4

while count < OPPORTUNITY:
    get_number = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(OPPORTUNITY - count)))
    if (get_number > 20 or get_number < 1):
        print("1-20 사이의 숫자를 입력하세요")
      	continue

    if get_number == answer:
    	print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(count+1))
        break
    elif get_number < answer:
      	print("Up")
    else:
      	print("Down")

    count += 1
    if (count == OPPORTUNITY):
      	print("아쉽습니다. 정답은 {}였습니다.".format(answer))