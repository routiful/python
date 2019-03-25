#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    numbers = []
    tries = 0
    while tries < 6:
        get_num = randint(1, 45)
        if get_num not in numbers:
            numbers.append(get_num)
            tries += 1
    
    return sorted(numbers)

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    numbers = generate_numbers()

    while len(numbers) < 7:
        bonus_num = randint(1, 45)
        if bonus_num not in numbers:
            numbers.append(bonus_num)

    return numbers        

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    for i in range(0, len(list1)):
        count += list2.count(list1[i])

    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    money = [1000000000, 50000000, 1000000, 50000, 5000]
    prize_money = 0
    # 일반 번호와의 일치 확인
    matching_count = count_matching_numbers(numbers, winning_numbers[0:6])
    if matching_count == 3:
        prize_money = money[4]
    elif matching_count == 4:
        prize_money = money[3]
    elif (matching_count == 5) and (count_matching_numbers(numbers, winning_numbers[6]) == 0):
        prize_money = money[2]
    elif (matching_count == 5) and (count_matching_numbers(numbers, winning_numbers[6]) == 1):
        prize_money = money[1]
    elif matching_count == 6:
        prize_money = money[0]
    else:
        prize_money = 0

    return prize_money