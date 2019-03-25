# 두 리스트 합치기
def merge(list1, list2):    
    new_list = []
    
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
        
    if i == len(list1):
        new_list += list2[j:]
    elif j == len(list2):
        new_list += list1[i:]
        
    return new_list    

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        return merge(merge_sort(my_list[:len(my_list)//2]), merge_sort(my_list[len(my_list)//2:]))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)