def get_lowest_not_in_list(l):
    n = 1
    while 1:
        if n not in l:
            break
        n += 1
        
    return n
         
l = [3, 4, -1, 1]

print(get_lowest_not_in_list(l))