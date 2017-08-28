from math import sqrt

def is_prime(x_value):
    """Check if x_value is a prime number."""
    if x_value < 2:
        return False
    for i in range(2, int(sqrt(x_value)) + 1):
        if x_value % i == 0:
            return False
    return True
