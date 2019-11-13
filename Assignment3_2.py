def createlist():
    size = int(input("Number of elements:"))
    nolist = list();
    for i in range(size):
        print("Input elements:",i+1)
        no=int(input());
        nolist.append(no);
    print("List is",nolist)
    return nolist;



def findmax(list1):
    max=list1[0];
    for num in list1:
        if max < num:
            max = num;
    return max;


if __name__ == "__main__":
    list1=createlist();
    print("Maximum number in list is",findmax(list1));


