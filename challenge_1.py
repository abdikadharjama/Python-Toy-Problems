def solution_challenge_1(A):
    """
    Calculates the minimum number of moves required to distribute bricks such that each box ends up with exactly 10 bricks.
    
    Parameters:
    A (list): A list of integers representing the number of bricks in each box.
    
    Returns:
    int: The minimum number of moves required, or -1 if it's impossible.
    """
    total_bricks = sum(A)
    box_count = len(A)
    required_bricks = 10 * box_count
    
    if total_bricks != required_bricks:
        return -1
    
    moves = 0
    for bricks in A:
        moves += max(0, bricks - 10)
    
    return moves

print(solution_challenge_1([7, 15, 10, 8]))