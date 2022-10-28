def bs(l, item, li, ri):
    mid=(li+ri)//2
    val =-1
    #print(l,item,li,ri)
    if(li>ri):
        return val
    if(item == l[mid]):
        val = mid
    elif(item>l[mid]):
        val = bs(l,item, mid+1,ri)
    elif(item<l[mid]):
        val = bs(l,item, li,mid-1)
    return val
def solve():
    n=int(input())
    trust=list(map(list,input().split()))
    ans=[]
    judge=[]
    for i in range(len(trust)):
        val=trust[i][0]
        val2=trust[i][1]
        if val not in ans:
            ans.append(val)
        judge.append(val2)
    #print(ans)
    if(len(ans)==n):
        return(-1)
    else:
        ans.sort()
        for i in range(1,n+1):
            value=bs(ans,i,0,len(ans)-1)
            #print(value)
            if value == -1:
                if(judge.count(i)==n):
                    return(i)
                else:
                    return -1
print(solve())
    
        
            
        
