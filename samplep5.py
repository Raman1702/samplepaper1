def pushZerosToEnd(a, n): 
    c = 0 
    for i in range(n): 
        if a[i] != 0:
            a[c] = a[i] 
            c+=1 
    while c < n: 
        a[c] = 0
        c += 1
a = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
n = len(a) 
pushZerosToEnd(a, n) 
print("Array after pushing all zeros to end of array:") 
print(a)
