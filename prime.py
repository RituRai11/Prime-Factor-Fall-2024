"""
prime.py -- Write the application code here
"""
def generate_prime_factors(n):
    """Generate prime factors of a number"""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n == 1:
        return []
    return []

def generate_prime_factors(n):
    """Generate prime factors of a number"""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n == 1:
        return []
    
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
