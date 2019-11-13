val=1
def fact(no):
    global val;
    if no!=0 :
        val=val*no;
        fact(no-1)
    return val


def main():
    no=int(input("Enter number"))
    result=fact(no)
    print("Factorial is ",result)

if __name__=="__main__":
    main();
