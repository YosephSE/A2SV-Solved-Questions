n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# res = []
# nums_less = 0

# for i in b:
#     while nums_less < n and a[nums_less] < i:
#         nums_less += 1
#     res.append(nums_less)

# print(*res)





def number_smaller(arr1, arr2):
    
    result=[]
    indx1, indx2 =0,0
    
    while indx1<len(arr1) and indx2 < len(arr2):
        if arr1[indx1] < arr2[indx2]:
            indx1+=1
        else:
            result.append(indx1)
            indx2+=1
    
    result.extend([len(arr1)] * (len(arr2) - len(result)))
    return ' '.join(map(str, result))


    
print(number_smaller(a,b))
    
