# find palidrom of string
# method 2. by using 2 pointers



def is_palidrom(s):
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False

        left +=1
        reight -=1
    return True




print(is_palidrom(s))
