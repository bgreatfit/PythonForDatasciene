def find_counts(arr, n):
    # Traverse all array elements
    i = 0
    while i < n:

        # If this element is already processed,
        # then nothing to do
        if arr[i] <= 0:
            i += 1
            continue

        # Find index corresponding to this element
        # For example, index for 5 is 4
        elementIndex = arr[i] - 1

        # If the elementIndex has an element that is not
        # processed yet, then first store that element
        # to arr[i] so that we don't loose anything.
        if arr[elementIndex] > 0:
            arr[i] = arr[elementIndex]

            # After storing arr[elementIndex], change it
            # to store initial count of 'arr[i]'
            arr[elementIndex] = -1

        else:

            # If this is NOT first occurrence of arr[i],
            # then increment its count.
            arr[elementIndex] -= 1

            # And initialize arr[i] as 0 means the element
            # 'i+1' is not seen so far
            arr[i] = 0
            i += 1

    print("Below are counts of all elements")
    for i in range(0, n):
        print("%d -> %d" % (i + 1, abs(arr[i])))
    print("")


arr = [2, 3, 3, 2, 5, 8, 9, 9]
find_counts(arr, len(arr))
