def run(l):
    final = []
    for i in range(len(l)):
        total = 0
        for f in range(len(l)):
            if i != f:
                if total == 0:            
                    total = l[f]
                else:
                    total *= l[f]
        final.append(total)
    return final

a = [1,2,3,4,5]

print(run(a))



