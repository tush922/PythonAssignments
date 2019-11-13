from functools import *

def filterdata(l):
    if l>=70 and l<=90:
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

def increase(l):
    return l+10

def mult(no1,no2):
    return no1*no2;



data=list(createlist())
print("Input List",data)
filtereddata=list(filter(filterdata,data))
print("List after filter",filtereddata)
increaseddata=list(map(increase,filtereddata))
print("List after map",increaseddata)
reduceddata=reduce(mult,increaseddata)
print("Output after reduce",reduceddata)