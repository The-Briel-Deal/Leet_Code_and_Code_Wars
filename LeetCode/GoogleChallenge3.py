


p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = []
# for xp in range(len(given)):
#     for yp in range(len(given)):
#         for zp in range(len(given)):
#             if xp != yp and xp != zp and yp != zp:
#                 if given[yp] % given[xp]  == 0 and given[zp] % given[yp] == 0:
#                     lt = [given[xp], given[yp], given[zp]]
#                     if not lt in c:
#                         c.append(lt)
def solution(l):
    s_length = len(l)
    c = ([0] * s_length)
    count = 0
    for i in range(0, len(l)):
        j = 0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count
        
print(solution(p))