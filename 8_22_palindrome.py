def is_palindrome(word):
    word_list = list(word)
    for index in range(int(len(word_list)/2)):
        temp = word_list[len(word_list)- index - 1] 
        word_list[len(word_list) - index - 1] = word_list[index]
        word_list[index] = temp
        
    new_word = ''.join(word_list)    
    
    if word == new_word:
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))