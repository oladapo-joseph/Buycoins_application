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
    i = x%y
    j = x//y 
    return (i,j)


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
    
    m_0 = m #the value of th
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        m_initial = m
        m, q = mod(a,m)
        # to continue the recursion
        a = m_initial
        y_initial = y
        # Update x and y
        y = x - q * y
        x = y_initial
 
    # Make x positive
    if (x < 0):
        x = x + m_0
 
    return x
 