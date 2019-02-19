print("enter the request queue:")
rq=list(map(int,input().split()))
rwh=int(input("enter the current positon of r/w head"))
l=[]
count=0
j=rwh
p=[]
s=[]
k=0
t=len(rq)
while count<t:
    for i in range(len(rq)):
        if rq[i]!=j and rq[i] not in p:
            l.append(abs(rq[i]-j))
            s.append(rq[i]-j)
    
    
    m=min(l)
    l.reverse()
    s.reverse()
    n=l.index(min(l))
    k=k+m
    p.append(j)
    j=j+s[n]
    l.clear()
    s.clear()
    count=count+1
print(k)

