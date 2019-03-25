# 삽입 정렬
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        for j in range(i, 0, -1):
            if temp <= my_list[j-1]:              
                my_list[j] = my_list[j-1]
                my_list[j-1] = temp
            elif temp > my_list[j-1]: 
                my_list[j] = temp
                break;
    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)