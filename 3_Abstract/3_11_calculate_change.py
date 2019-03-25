#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def calculate_change(payment, cost):
    change = payment - cost
    print('50000원 지폐: {0}장'.format(int(change/50000)))
    change = change%50000
    print('10000원 지폐: {0}장'.format(int(change/10000)))
    change = change%10000
    print('5000원 지폐: {0}장'.format(int(change/5000)))
    change = change%5000
    print('1000원 지폐: {0}장'.format(int(change/1000)))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)