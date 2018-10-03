# Nick Furlo
# CSI 3610
# October 2nd 2018

# This method finds the first 0 inside the given array. It checks the midpoint of the array for 0 or 1. If it is a zero,
# it will then do the same check on the left half of the array. If it is a one, it will check the midpoint of the right
# half. Once the starting index of the array is equal to the middle index of the array, that index is the location of
# the first 0.
def findSymbol(arr, min, max):
    global index
    # This print shows you the array being narrowed down
    print("\n\nMin: " + str(min) + "\nMax: " + str(max))

    # These statments calculate a midpoint for the subarray
    temp = int((max - min) / 2)
    mid = min + temp
    print("2MID: " + str(mid))

    # Check to see if index has been found
    if (min == mid) or (max == mid):
        index = max
        return

    # This if checks to see if the midpoint is a 0 or 1. If it is a 0 we know the rest of the elements to the right will
    # be 0's, so we need to check the elements behind us. If the midpoint is a 1 we know the rest of the elements to the
    # left will be 1's, so we need to check the elements ahead of us.
    # It then makes a recursive call but with a new subarray specified.
    if arr[mid] == 0:
        findSymbol(arr, min, mid)
    else:
        findSymbol(arr, mid, max)


ar = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, ]
n = len(ar) - 1

index = -1
print("Array: " + str(ar))
findSymbol(ar, 0, n)
print("The index of the first 0 is " + str(index))
print("The array has " + str(n) + " elements")
