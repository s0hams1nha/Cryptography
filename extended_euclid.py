def extended_euclid(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while(r2!=0):
        q = r1//r2

        r = r1 - q*r2
        r1=r2
        r2=r

        s = s1 - q*s2
        s1 = s2
        s2 = s

        t = t1 - q*t2
        t1 = t2
        t2 = t

    print(f"GCD of {a} and {b} is: ", r1, "\n", "Value of s is: ", s1, "\n", "Value of t is: ", t1)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
extended_euclid(a, b)