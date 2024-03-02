def solution_challenge_3(N):
    """
    Generates a string of length N containing as many different lower-case letters as possible, each occurring an equal number of times.
    
    Parameters:
    N (int): The length of the string to generate.
    
    Returns:
    str: A string where each letter occurs an equal number of times, or an empty string if not possible.
    """
    if N > 26:
        # Find the highest factor of N that is 26 or lower
        for factor in range(26, 0, -1):
            if N % factor == 0:
                repeat_count = N // factor
                return ''.join([chr(97 + i) * repeat_count for i in range(factor)])
    elif N <= 26:
        return ''.join([chr(97 + i) for i in range(N)])
    
    return ""


if __name__ == "__main__":
   
    # Challenge 3
    print(solution_challenge_3(5))
