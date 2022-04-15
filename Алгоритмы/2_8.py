# Write a function that reverses a string. The input string is given as an array of characters such.
# You must do this by modifying the input array in-place with O(1) extra memory.

def rev_list(a:list):
    new_l = ['0'] * len(a)

    def helper(a, j):
        m = 0
        if j >= len(a) // 2:
            return
        helper(a, j + 1)
        a[j], a[-1 - j] = a[-1 - j], a[j]

    helper(a, 0)
    return a


print(rev_list(['a', 'b', 'c', 'd', 'e']))
