#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
new_file = open('vocabulary.txt', 'w')

while True:
    eng_word = input("영어 단어를 입력하세요: ")
    if eng_word == 'q':
        break
    kor_word = input("한국어 뜻을 입력하세요: ")

    new_file.write(eng_word + ': ')
    new_file.write(kor_word + '\n')
    
new_file.close()