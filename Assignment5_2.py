def dis(no):
    if no!=0 :
        dis(no-1)
        print(no, end=" ")

def main():
    no=int(input("Enter number"))
    dis(no)

if __name__=="__main__":
    main();
