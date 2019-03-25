def mask_security_number(security_number):
#    result = security_number[ : -4]
#    result = result + '****'
#    return result
    security_number_list = list(security_number)
    for index in range(0, 4):
        num_length = len(security_number_list)
        security_number_list[num_length - index - 1] = '*'
        
    result_str = ""
    for index in range(len(security_number_list)):
        result_str += security_number_list[index]
    
    return result_str

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))