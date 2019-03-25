#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from random import randint

ENG = 0
KOR = 1

in_file = open('vocabulary.txt', 'r')
vocabulary = {}

for line in in_file:    
    words = line.strip().split(": ")
    vocabulary[words[KOR]] = words[ENG]

kor_words = list(vocabulary.keys())
while True:
    question_word = kor_words[randint(0, len(kor_words) - 1)]
    get_eng_word = input(question_word + ': ')
    if get_eng_word == 'q':
        break

    if get_eng_word == vocabulary[question_word] :
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(vocabulary[question_word]))

in_file.close()