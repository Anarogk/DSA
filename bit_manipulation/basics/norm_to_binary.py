# Normal to Binary
def norm_to_binary(num):
    strg = ""
    while num>0:
        add = num%2 # add term is the remainder at each division by 2
        strg= str(add)+ strg # add the add term at the start of empty string
        num = num//2 # perform floor division of num to get divedent integer 
    return strg
     

def main():
    print(norm_to_binary(23))


if __name__ == "__main__":
    main()
