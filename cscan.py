print("enter the request queue:")
rq=list(map(int,input().split()))
rwh=int(input("enter the current positon of r/w head "))
p=int(input("enter the last value of r/w head "))
q=int(input("enter the initial value of r/w head "))
rq.sort()
for i in range(len(rq)):
    if rq[i]<=rwh:
        n=i
    else:
        break
k=(p-rwh)+p-q + rq[n]-q
print("total no of track movements:",end=' ')
print(k)