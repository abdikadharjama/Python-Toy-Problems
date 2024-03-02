def digit_sum(n):
    """Helper function to calculate the sum of digits of a number."""
    return sum(map(int, str(n)))

def solution_challenge_2(A):
    """
    Finds the maximum sum of two numbers whose digits add up to an equal sum.
    
    Parameters:
    A (list): A list of integers.
    
    Returns:
    int: The maximum sum of two numbers with equal digit sum, or -1 if no such pair exists.
    """
    sums = {}
    for num in A:
        s = digit_sum(num)
        if s not in sums:
            sums[s] = [num]
        else:
            sums[s].append(num)
            sums[s] = sorted(sums[s], reverse=True)[:2]
    
    max_sum = -1
    for key in sums:
        if len(sums[key]) > 1:
            max_sum = max(max_sum, sum(sums[key][:2]))
    
    return max_sum

print(solution_challenge_2([51, 71, 17, 42]))