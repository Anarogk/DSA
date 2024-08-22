# if we perform bitwise operation on two integers then it is automatically 
# converted to binary and operation is performed.

def main():
    print(25&13) # and operator
    print(25|13) # or operator
    print(25^13) # xor operator
    print(~13) # negation operator

    print(bin(25)) # print the binary of that number

if __name__ == "__main__":
    main()