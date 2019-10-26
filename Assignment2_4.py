def add(num):
    no=0;
    for i in range(num+1):
        no = no+i
    return no;


num=add(int(input("Enter number ")))
print("Addition of numbers is ",num)
