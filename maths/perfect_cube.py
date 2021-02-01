def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.
    >>> perfect_cube(6848175699)
    True
    >>> perfect_cube(4)
    False
    """
    val = n ** (1 / 3)
    if ((int(val)**3 == n) or (int(val+1)**3 == n)):
        return True
    else:
        return False

if __name__ == "__main__":
    print(perfect_cube(6848175699))
    print(perfect_cube(4))
