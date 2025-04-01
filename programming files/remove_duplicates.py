def remove_duplicates(arr):
    arr.sort()
    unique_arr = []
    removed_elements = []
    # iterate through array, if element not already included in unique_arr then add it
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i+1]:
            unique_arr.append(arr[i])
        else:
            removed_elements.append(arr[i])
    return unique_array, removed_elements
# creates an array and removes any duplicate values, storing them in a new array
# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
