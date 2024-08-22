num = int(input("Enter any Number"))
d = {
    1000: "M", 900:"CM", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X",
    9:"IX", 5:"V", 4:"IV",  1:"I"
}

res =""
for i, n in dict.items():
    while num>=i:
        res+=n
        num -=n
print(res)