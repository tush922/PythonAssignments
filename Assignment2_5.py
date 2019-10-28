def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print("Its not a prime number")
                break
            else:
                print(num,"is prime number")
                break
    else:
        print(num,"is not a prime number")



num=prime(int(input("Enter number ")))
