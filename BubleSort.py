def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0 , n-i - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]

    return arr

print(buble_sort([5,3,8,4,2]))