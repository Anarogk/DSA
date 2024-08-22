def intToRoman(num: int) -> str:
    map = [1000, 900, 500, 400, 100, 90 , 50 , 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L","XL","X","IX","V","IV","I"]
    i=0
    res = ''
    while num> 0:
        if num >map[i]:
            res+=rom[i]
        else:
            num -= rom[i]
        i+=1
    return res