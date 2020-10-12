def maxList(l):
    """Function to figure out the max value in a list is called."""
    a = [int(i) for i in l.split()]
    print("The maximum value in the list is:", end=" ")
    return max(a)


lst = input("Enter Numbers to a list separated by a space:")
print(maxList.__doc__)
print(maxList(lst))

