if __name__ == '__main__':
    n = int(input())
    integer_list = input().split()
    for num in integer_list:
        num1 = integer_list[0]
        num2 = integer_list[1]
        t = num1, num2
        print(hash(t))
