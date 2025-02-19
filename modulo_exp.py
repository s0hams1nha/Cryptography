def mod_exponentiation(a, b, m):
    result = 1
    a = a%m

    while(b>0):
        if b%2==1:
            result = (result*a)%m
        a = (a*a)%m
        b//=2

    print("Result is: ", result)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))

mod_exponentiation(a, b, m)