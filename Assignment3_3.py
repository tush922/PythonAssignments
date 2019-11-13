def createlist():
    size = int(input("Number of elements:"))
    nolist = list();
    for i in range(size):
        print("Input elements:",i+1)
        no=int(input());
        nolist.append(no);
    print("List is",nolist)
    return nolist;


def findmin(list1):
    min=list1[0];
    for num in list1:
        if min > num:
            min = num;
    return min;


if __name__ == "__main__":
    list1=createlist();
    print("Minimum number in list is",findmin(list1));


