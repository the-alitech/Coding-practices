# find string is palidrom or not
# method one by using slicing


def is_palidrom(s):
    
    if len(s) == 0 or len(s) < 0:
        return False

    shift_string = s[::-1]

    if shift_string == s:
        return True
    return False


st = is_palidrom("abba")
