def fizzbuzz(x):
    """Take integer and check if it is divisable by:
        3: return 'fizz',
        5: return 'buzz',
        3 and 5: return 'fizzbuzz',
        otherwise: return input as string.

	Args:
		x: The integer for which the condition is checked.

	Returns:
		Corresponding string value.
    """
    if x % 3 == 0 and x % 5 == 0:
        return "fizzbuzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    else:
        return str(x)
