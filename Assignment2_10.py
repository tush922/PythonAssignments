def add(num):
    total=0;
    for i in range(len(num)):
        total=total+int(num[i])
    return total

x=add(list(input("Enter number")))
print("Addition of number is",x)
