def swapValues(l):
    """Function to swap with first and last value in a list is called."""
    a = [int(i) for i in l.split()]
    a[0], a[-1] = a[-1], a[0]
    print("After swapping the first and last value the list is:", end=" ")
    return a


lst = input("Enter Numbers to a list separated by a space:")
print(swapValues.__doc__)
print(swapValues(lst))

