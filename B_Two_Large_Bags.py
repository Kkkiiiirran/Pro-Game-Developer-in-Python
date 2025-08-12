
# for _ in range(int(input())):
#     n= int(input())

#     arr = list(map(int,input().split()))
#     arr.sort()
#     all_even = True
#     mp = {}
#     for i in range(n):
#         mp[arr[i]] = mp.get(arr[i],0)+1
    
#     maxi = arr[-1]
#     # if len(mp)%n==1:
#     #     print("No")
#     #     continue

#     for num in mp:
#         if mp[num]%2:
#             all_even = False
        
#     if all_even:
#         print("YES")
#         continue
    
#     for num in mp:
#         if num != maxi:
#             temp = (maxi-num)*2
#             if mp[num]<temp:
#                 print("No")
#                 break
#     else:
#         print("Yes")

