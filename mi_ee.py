def gcd_euclid(a, n):
    r1 = a
    r2 = n

    while(r2!=0):
        q = r1//r2
        r = r1 - q*r2
        r1 = r2
        r2 = r
    
    return r1


def mi_ee(a, n):
    if(gcd_euclid(a, n) != 1):
        print("The GCD is: ", gcd_euclid(a, n))
        print("No multiplicative inverse")
    else:
        r1 = n
        r2 = a
        t1 = 0
        t2 = 1

        while(r2!=0):
            q = r1//r2
            r = r1 - q*r2
            r1 = r2
            r2 = r

            t = t1 - q*t2
            t1 = t2
            t2 = t

        if(t1<0):
            t1+=n
        print(f"The GCD is {r1}", "\n", f"The multiplicative inverse is {t1}")

a = int(input("Enter a: "))
n = int(input("Enter n: "))
mi_ee(a, n)