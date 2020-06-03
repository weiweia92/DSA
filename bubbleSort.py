def bubbleSort(ar):
    n = len(ar)
    for i in range(n-1):
        for j in range(n-i-1):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
    return ar

ar = [64, 34, 25, 12, 22, 11, 90] 
print(bubbleSort(ar))
            
