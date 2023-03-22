def find_t_low(areaCalculation, t_min, t_max, alpha, del_t):
    """
    Finds t_low for areaCalculation(t) using binary search.

    Args:
        areaCalculation (function): A function that takes a parameter t between t_min and t_max and returns a value between 0 and 1.
        t_min (float): The minimum value of the parameter t.
        t_max (float): The maximum value of the parameter t.
        alpha (float): The target value of areaCalculation(t) for t_low.
        del_t (float): The tolerance for the difference between the two solutions for t_low.

    Returns:
        t_low (float): The value of the parameter t such that areaCalculation(t) = alpha.
    """
    # Initialize the bounds of the search range.
    low = t_min
    high = t_max

    # Perform binary search until two solutions for t_low are found and the difference between them is less than the tolerance.
    while True:
        # Calculate the midpoint of the search range.
        mid = (low + high) / 2

        # Evaluate the function at the midpoint and the endpoints.
        f_low = areaCalculation(low)
        f_mid = areaCalculation(mid)
        f_high = areaCalculation(high)

        # Check if the target value has been found.
        if abs(f_mid - alpha) < del_t and abs(f_low - alpha) < del_t:
            # Check if the two solutions are close enough.
            if abs(mid - low) < del_t:
                return mid
            elif abs(high - mid) < del_t:
                return low
            else:
                return (low + mid) / 2

        # Update the bounds of the search range.
        if f_mid < alpha:
            low = mid
        else:
            high = mid