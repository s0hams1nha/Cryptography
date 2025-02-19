def gcd_euclid(a, n):
    r1 = n
    r2 = a
    t1 = 0
    t2 = 1

    while(r2!=0):
        q = r1//r2
        r = r1 - r2*q
        r1 = r2
        r2 = r

        t = t1 - t2*q
        t1 = t2
        t2 = t

    return r1 

def mod_exp(a, b, m):
    result = 1
    a = a%m

    while(b>0):
        if(b%2==1):
            result = (result*a)%m
        a = (a*a)%m
        b//=2
    return result

def phi(m):
    count = 0
    for i in range(1, m):
        if gcd_euclid(i, m) == 1:
            count+=1
    return count

def mi_euler(a, n):
    if gcd_euclid(a, n)!=1 or n<0:
        print(f"GCD of {a} and {n} is not 1, they are not co-prime AND/OR n is negative")
    else:
        print("The result is: ", mod_exp(a, phi(n)-1, n))

a = int(input("Enter a: "))
n = int(input("Enter n: "))
mi_euler(a, n)