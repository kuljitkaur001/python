def has_4_uppercase(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
        if count >= 4:
            return True
    return False
     