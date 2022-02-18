# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

new_n = []
def new_f(n:int, j=0):
    j2 = 2 ** j
    if j2 not in new_n:
        new_n.append(j2)
    if new_n[-1] < n:
        new_f(n, j+1)
    return n in new_n
print(new_f(8))
print(new_f(18))
print(new_f(31))
print(new_f(64))
print(new_f(256))

