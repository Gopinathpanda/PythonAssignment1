def secondMaxList(l):
    """Function to figure out the second max value in a list is called."""
    a = [int(i) for i in l.split()]
    a.remove(max(a))
    print("The second maximum value in the list is:", end=" ")
    return max(a)


lst = input("Enter Numbers to a list separated by a space:")
print(secondMaxList.__doc__)
print(secondMaxList(lst))
