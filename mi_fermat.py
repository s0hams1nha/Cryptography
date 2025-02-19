def mod_exponentiation(a, b, m):
    result = 1
    a = a%m

    while(b>0):
        if(b%2==1):
            result = (result*a) % m
        a = (a*a)%m
        b//=2
    return result

def is_prime(p):
    for i in range(2, p//2):
        if p%i==0:
            return False
    return True

def multiplicative_inverse(a, p):
    if a % p == 0:
        return "Inverse does not exist and/or not possible to calculate through Fermat's"  # No inverse if a is divisible by p
    if not is_prime(p):
        return "Inverse does not exist and/or not possible to calculate through Fermat's"
    
    return mod_exponentiation(a, p - 2, p)  # Compute a^(p-2) % p

# Example usage:
a = int(input("Enter number (a): "))
p = int(input("Enter prime modulus (p): "))

if p <= 1:
    print("Modulus must be a prime number greater than 1.")
else:
    print(f"Multiplicative Inverse of {a} mod {p} is: {multiplicative_inverse(a, p)}")
