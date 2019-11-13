def dis(no):
    if no!=0 :
        print(no, end=" ")
        dis(no-1)


def main():
    no=int(input("Enter number"))
    dis(no)

if __name__=="__main__":
    main();
