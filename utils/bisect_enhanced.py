import bisect

def binary_search_left(a, x, lo=0, hi=None):
    """Return index of left most occurrence of x in list a (assuming a is sorted),if 
    element x is not found in the list a return -1
    
        If a non-negative value i is returned, list a is gaurenteed to have the value x at index i
    
        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_left(a, x, lo, hi)
    if l != len(a) and a[l] == x:
        return l
    return -1


def binary_search_right(a, x, lo=0, hi=None):
    """Return index of right most occurrence of x in list a (assuming a is sorted),if 
    element x is not found in the list a return -1
    
        If a non-negative value i is returned, list a is gaurenteed to have the value x at index i
    
        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_right(a, x, lo, hi) - 1
    if l != -1 and a[l] == x:
        return l
    return -1


def next_lower(a, x, lo=0, hi=None):
    """Return the index of rightmost element lower than the element x in the list a. 
    If no such element exists, should return -1.

        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_right(a, x, lo, hi) - 1
    if l != -1 and a[l] == x:
        l = bisect.bisect_left(a, x, lo, hi) - 1
    return l


def next_lower_or_eq(a, x, lo=0, hi=None):
    """Return the index of rightmost element lower than or equal to the element x in the list a. 
    If no such element exists, should return -1.

        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_right(a, x, lo, hi)
    if l != -1 and a[l] != x:
        l -= 1
    return l


def next_higher(a, x, lo=0, hi=None):
    """Return the index of leftmost element higher than the element x in the list a. 
    If no such element exists, should return -1.

        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_right(a, x, lo, hi)
    if l != len(a):
        return l
    return -1


def next_higher_or_eq(a, x, lo=0, hi=None):
    """Return the index of leftmost element higher than or equal to the element x in the list a. 
    If no such element exists, should return -1.

        Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if hi is None: hi = len(a)
    l = bisect.bisect_left(a, x, lo, hi)
    if l != len(a):
        return l
    return -1


if __name__ == "__main__":
    assert binary_search_left([1, 2, 2, 5, 6], 2) == 1
    assert binary_search_left([1, 2, 2, 5, 6], 3) == -1

    assert binary_search_right([1, 2, 2, 5, 6], 2) == 2
    assert binary_search_right([1, 2, 2, 5, 6], 7) == -1

    assert next_lower([1, 2, 2, 5, 6], 3) == 2
    assert next_lower([1, 2, 2, 5, 6], 2) == 0
    assert next_lower([1, 2, 2, 5, 6], 0) == -1

    assert next_lower_or_eq([1, 2, 2, 5, 6], 3) == 2
    assert next_lower_or_eq([1, 2, 2, 5, 6], 2) == 2
    assert next_lower_or_eq([1, 2, 2, 5, 6], 0) == -1

    assert next_higher([1, 2, 2, 5, 6], 1) == 1
    assert next_higher([1, 3, 3, 5, 6], 2) == 1
    assert next_higher([1, 3, 3, 5, 6], 3) == 3
    assert next_higher([1, 2, 2, 5, 6], 7) == -1

    assert next_higher_or_eq([1, 2, 2, 5, 6], 1) == 0
    assert next_higher_or_eq([1, 3, 3, 5, 6], 2) == 1
    assert next_higher_or_eq([1, 3, 3, 5, 6], 3) == 1
    assert next_higher_or_eq([1, 3, 3, 5, 6], 4) == 3
    assert next_higher_or_eq([1, 2, 2, 5, 6], 7) == -1
