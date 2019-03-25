#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

ENG = 0
KOR = 1

in_file = open('vocabulary.txt', 'r')

for line in in_file:
    words = line.strip().split(": ")
    get_word = input(words[KOR] + ': ')

    if get_word == words[ENG]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(words[ENG]))

in_file.close()