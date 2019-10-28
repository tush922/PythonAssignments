def disp(num):
    for i in range(num):
       for j in range(1,num+1):
            print(j,end=' ')
       print()


disp(int(input("Enter number")))