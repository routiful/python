# 선택 정렬
def selection_sort(my_list):
    count = 0    
    index_of_min = 0
    
    while count < len(my_list) - 1:
        min_val = my_list[count]
        
        for i in range(count, len(my_list)):
            if my_list[i] <= min_val:
                min_val = my_list[i]
                index_of_min = i
                
        temp = my_list[count]
        my_list[count] = my_list[index_of_min]
        my_list[index_of_min] = temp        
        count += 1
        
    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)