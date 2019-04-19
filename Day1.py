def run(l,k):
    for i in l:
        for f in l:
            if i + f == k:
                return True
    return False

def run2(l,k):
    a = []
    for i in l:
        for f in a:
            if f == i:
                return True
        a.append(k-i)
    return False

