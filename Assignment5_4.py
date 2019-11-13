def add(no):
    if no==0:
        return 0
    return no%10+add(int(no/10))


def main():
    no=int(input("Enter number"))
    result=add(no)
    print(result)
    

if __name__=="__main__":
    main();
