def createlist():
    size = int(input("Number of elements:"))
    nolist = list();
    for i in range(size):
        print("Input elements:",i+1)
        no=int(input());
        nolist.append(no);
    print("List is",nolist)
    return nolist;


def checkfrequncy(no,list1):
    search=no;
    i=0;
    for num in list1:
        if search == num:
            i=i+1;
    return i;


if __name__ == "__main__":
    list1=createlist();
    no=int(input("Element to search:"))
    print("Output:",checkfrequncy(no,list1));


