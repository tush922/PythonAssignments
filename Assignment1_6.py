def chknum(num):
    if 0==num:
        print("Zero ");
    elif 0<num:
        print("Positive Number");
    else:
        print("Negative Number");


print("Enter number");
num=int(input());
chknum(num);

