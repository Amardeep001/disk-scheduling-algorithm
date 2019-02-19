print("enter the request queue:")
rq=list(map(int,input().split()))
rwh=int(input("enter the current positon of r/w head"))
k=0
for i in range(len(rq)):
    if i==0:
        k=k+abs(rq[i]-rwh)
    else:
        k=k+abs(rq[i]-rq[i-1])

print("total no of track movements:",end=' ')
print(k)
