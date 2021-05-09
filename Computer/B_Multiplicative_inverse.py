


def mod(x,y):
    """
        Args:

        x : int
            an integer input

        y : int 


        Returns: 
        i : int
            modulus of x and y
        
        j : int
            divisor of x and y
    
    
    """
    return ( x%y, x//y)

numbers = []

def multi_inverse(a,b):
    """
        Args:

        a :  int

            one of the input integers in the equation,

        b : int

            the second integer in the equation
        
    
        Returns:

        final : int
                the final modulo 
        
        gcd   : int

            returns the gcd of the two inputs
             
    """
    try:
        if isinstance(a, int) and isinstance(b, int) :
            pass
    except TypeError as e:
        return e
    numbers.append(a)
    numbers.append(b)
    
    if a>b:
        modulo, var = mod(a,b)
        # print(modulo)
        numbers.append(modulo)
        while modulo != 0:
            modulo, _ = multi_inverse(numbers[-2], modulo)
     
    final = modulo
    gcd = numbers[-2]
    return (final, gcd)


_ ,gcd = multi_inverse(6, 2)
print(gcd)

print(numbers[-2])

def modInverse(a, m):
    """
        Args:

        a :  int

            one of the input integers in the equation,

        m : int

            the second integer in the equation
        
    
        Returns:
            x : int
                multiplicative inverse of a, using Euclidean Algorithm 
                ax (mod) m = 1    
    """        
    
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
    if a>m:
        _, gcd = multi_inverse(a, m)
    if m>a:
        _, gcd = multi_inverse(m, a)

    if gcd ==a :
        return 'The values are not coprimes'
    else:
            
        while (a > 1):
    
            # q is quotient
            m1 = m
            m, q = mod(a,m)
            a = m1
            t = y
            # Update x and y
            y = x - q * y
            x = t
    
        # Make x positive
        if (x < 0):
            x = x + m0
    
        return x
 
print(modInverse(2,7))