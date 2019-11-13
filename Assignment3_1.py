def storeandadd():
    size = int(input("Enter size for list"))
    nolist = list();
    addition=0;
    for i in range(size):
        print("Enter number",i+1)
        no=int(input());
        addition=addition+no;
        nolist.append(no);
    print("List is",nolist)
    print("Addition is", addition)
    return nolist;


if __name__ == "__main__":
    storeandadd();


