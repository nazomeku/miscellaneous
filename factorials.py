def rFactorial(x):
    """Recursive take on factorial computing problem."""
    if x in (0, 1):
        return 1
    else:
        return x * rFactorial(x-1)

def iFactorial(x):
    """Iterative take on factorial computing problem."""
    if x in (0, 1):
        return 1
    else:
        result = 1
        for i in range(2, x+1):
            result *= i
        return result
