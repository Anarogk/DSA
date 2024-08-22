def reverse_string(s):
    for i in range(len(s)//2):
        s = s[i:] + s[:i]
    return s
s = "hello hwo are you! fine thank you"
print(reverse_string(s))