from functools import *

def chkeven(no):
    if no%2==0:
        return True;
    else:
        return False;

def createlist():
    size = int(input("Number of elements:"))
    nolist = list();
    for i in range(size):
        print("Input elements:",i+1)
        no=int(input());
        nolist.append(no);
    print("List is",nolist)
    return nolist;

def squ(no):
    return no*no;

def add(no1,no2):
    return no1+no2;



data=list(createlist())
print("Input List ",data)
filtereddata=list(filter(chkeven,data))
print("List after filter ",filtereddata)
increaseddata=list(map(squ,filtereddata))
print("List after map",increaseddata)
reduceddata=reduce(add,increaseddata)
print("Output of reduce",reduceddata)

