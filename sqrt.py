def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria.

	Args:
		x: The number for which the square roots is to be computed.

	Returns:
		The square root of x.

	Raises:
		ValueError: If x is negative.
	"""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    temp = x
    i = 0
    while temp * temp != x and i < 20:
        temp = (temp + x / temp) / 2.0
        i += 1
    return temp
