def mi_eulid(a, n):
    r1 = n
    r2 = a
    t1 = 0
    t2 = 1
    while(r2>0):
        q = r1//r2
        r = r1 - r2*q
        r1 =r2
        r2 = r

        t = t1 - t2*q
        t1 = t2
        t2 = t
    
    return t1

def gcd_eulid(a, n):
    r1 = n
    r2 = a
    t1 = 0
    t2 = 1
    while(r2>0):
        q = r1//r2
        r = r1 - r2*q
        r1 =r2
        r2 = r
    return r1

def crt(a1, a2, a3, m1, m2, m3):

    if gcd_eulid(m1, m2)!=1 or gcd_eulid(m2, m3)!=1 or gcd_eulid(m3, m1)!=1:
        return "NA"

    M = m1*m2*m3
    M1 = M//m1
    M2 = M//m2
    M3 = M//m3

    M1_inv = mi_eulid(M1, m1)
    M2_inv = mi_eulid(M2, m2)
    M3_inv = mi_eulid(M3, m3)

    return ((a1*M1*M1_inv) + (a2*M2*M2_inv) + (a3*M3*M3_inv))%M

a1 = int(input("Enter a1: "))
a2 = int(input("Enter a2: "))
a3 = int(input("Enter a3: "))

m1 = int(input("Enter m1: "))
m2 = int(input("Enter m2: "))
m3 = int(input("Enter m3: "))

print(crt(a1, a2, a3, m1, m2, m3))