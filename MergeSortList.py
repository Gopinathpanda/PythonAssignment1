def mergeSortList(l1, l2):
    """Function to merge and sort two lists."""
    a = [int(i) for i in l1.split()]
    b = [int(i) for i in l2.split()]
    a.extend(b)
    a.sort()
    print("After merging and sorting the new list is:", end=" ")
    return a


lst1 = input("Enter Numbers to the first list separated by a space:")
lst2 = input("Enter Numbers to the second list separated by a space:")
print(mergeSortList.__doc__)
print(mergeSortList(lst1, lst2))
