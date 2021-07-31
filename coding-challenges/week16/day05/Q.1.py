# 1) Write a Program to find the largest element in an arrray

# Example:
# Input : arr[] = {10, 20, 4}
# Output : 20

# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100


def getLargestElement(arr, n):
    large = arr[0]
    for i in range(1, n):
        if arr[i] > large:
            large = arr[i]

    return large


if __name__ == "__main__":
    arr = [20, 10, 20, 4, 100]
    n = len(arr)
    ans = getLargestElement(arr, n)
    print(f'Largest element in an arrray', ans)
