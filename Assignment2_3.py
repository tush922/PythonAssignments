def factorial(num):
    fact=1;
    for i in range(1,num+1):
        fact = fact*i
    return fact;


fact=factorial(int(input("Enter number for factorial")))
print("factorial is ",fact)