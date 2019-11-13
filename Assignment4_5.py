from functools import *

def chkprime(num):
    for i in range(2, num//2):
        if (num % i) == 0:
            return False;
            break
    else:
        return True;


def createlist():
    size = int(input("Number of elements:"))
    nolist = list();
    for i in range(size):
        print("Input elements:",i+1)
        no=int(input());
        nolist.append(no);
    print("List is",nolist)
    return nolist;


def mult(no):
    return no*2;


def maxno(no1,no2):
    if no1<no2:
        return no2


data=list(createlist())
print("Input List ",data)
filtereddata=list(filter(chkprime,data))
print("List after filter ",filtereddata)
mapdata=list(map(mult,filtereddata))
print("List after map",mapdata)
reduceddata=reduce(maxno,mapdata)
print("Output of reduce",reduceddata)