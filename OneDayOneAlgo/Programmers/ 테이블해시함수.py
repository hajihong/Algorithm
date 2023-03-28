data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]


data.sort(key= lambda x : (x[1],-x[0]))

print(data)
row_begin = 2
row_end = 3
arr = []
for i in range(row_begin-1, row_end):
    tmp = data[i]
    cnt = 0
    for elem in tmp:
        result = elem % (i+1)
        cnt += result
    arr.append(cnt)
    
standard= arr[0]
for i in range(len(arr)-1):
    standard = standard ^ arr[i+1]


    
print(standard)