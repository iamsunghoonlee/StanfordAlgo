def karatsuba(x: int, y: int, n: int):
    
    # 1. Organize numbers
    a = x // 10**(n/2)
    b = x % 10**(n/2)
    
    c = y // 10**(n/2)
    d = y % 10**(n/2)
    
    
    # 2. Set Base Case & Recursively Compute ac, ad, bc, bd
    if n/2 > 1:
        return (10**n)*karatsuba(a, c, n/2) + (10**(n/2))*(karatsuba(a, d, n/2) 
        + karatsuba(b, c, n/2)) + karatsuba(b, d, n/2)
    else:
        return (10**n)*a*c + (10**(n/2))*(a*d + b*c) + b*d

def main():
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    print(int(karatsuba(a, b, 64)))

if __name__ == '__main__':
    main()