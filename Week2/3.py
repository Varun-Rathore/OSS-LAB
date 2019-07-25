def duplicate(a):
    b=[]
    for i in a:
        cnt=0
        for j in b:
            if i==j:
                cnt=1
                break;
        if cnt==0:
            b.append(i)
    k=int(len(a)-len(b))
    print(k)
a=["hello","gaga","maga","hello","gaga","hello"]
duplicate(a)
