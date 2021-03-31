def swap_case(s):
    str2 = ''

    for ch in s:
        if 'a'<=ch<='z' or 'A'<=ch<='Z':
            str2 += chr(ord(ch)^32)
        else:
            str2 += ch
    return str2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)