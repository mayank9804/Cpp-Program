def isprime(n):
    k=[]
    for i in range(2,int(n**0.5)+1):
        while n%i==0:
            k.append(i)
            n//=i
    if n>1:
        k.append(n)
    k.sort()
    return k[-1]
    

z=int(input())
p=[]
i=1
c=0
while True:
        if isprime(i*i+1)>=2*i:
            c+=1
            p.append(i)
            if c==z:
                break
        i+=1
print(set(p))
