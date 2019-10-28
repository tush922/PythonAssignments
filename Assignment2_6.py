def disp(num):
    for i in range(num,0,-1):
        for j in range(i):
            print("*", end=' ')
        print()


disp(int(input("Enter a number")))