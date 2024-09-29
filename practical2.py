# Max-Min algorithm using Divide and Conquer principle
def find_max_min(arr, low, high):
    # If the array contains only one element
    if low == high:
        return (arr[low], arr[low])  # (max, min)

    # If the array contains two elements
    elif high == low + 1:
        if arr[low] > arr[high]:
            return (arr[low], arr[high])  # (max, min)
        else:
            return (arr[high], arr[low])  # (max, min)

    else:
        # Find the middle index
        mid = (low + high) // 2

        # Recursively find the maximum and minimum of both halves
        left_max, left_min = find_max_min(arr, low, mid)
        right_max, right_min = find_max_min(arr, mid + 1, high)

        # Combine the results
        final_max = max(left_max, right_max)
        final_min = min(left_min, right_min)

        return (final_max, final_min)

# Example usage:
arr = [100, 11, 445, 1, 330, 3000]
n = len(arr)
max_val, min_val = find_max_min(arr, 0, n - 1)
print("Maximum:", max_val)
print("Minimum:", min_val)
