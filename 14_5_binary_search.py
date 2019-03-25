def binary_search(element, some_list):    
    first = 0
    last = len(some_list) - 1
    
    while last - first >= 1:
        if last - first == 1:
            if element == some_list[first]:
                return first
            elif element == some_list[last]:
                return last
            else:
                return None
        else:
            mid = (first + last) // 2
            if element < some_list[mid]:
                last = mid - 1
            elif element > some_list[mid]:
                first = mid + 1
            else:
                return mid    
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))