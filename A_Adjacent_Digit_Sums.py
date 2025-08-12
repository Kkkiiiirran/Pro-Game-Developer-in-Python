

for _ in range(int(input())):
    x,y= map(int, input().split())
    if y==x+1:
        print("Yes")
    else:
        temp = x-y+1
        if temp>=9 and temp% 9==0:
            print("Yes")
        else:
            print("No")